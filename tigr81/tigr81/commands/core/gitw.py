import pathlib as pl
import shutil
import subprocess
import tempfile
from typing import Optional, Tuple

import typer


def get_author_info() -> Tuple[str, str]:
    """
    Retrieves the author's name and email from the Git configuration.

    Returns:
        Tuple[str, str]: A tuple containing the author's name and email.
    """
    # Get the author's email from Git config
    author_email = subprocess.run(
        ["git", "config", "user.email"], capture_output=True, text=True, check=True
    ).stdout.strip()

    # Extract the author's name from the email
    author_name = author_email.split("@")[0]

    return author_name, author_email


class DestinationFolderError(Exception):
    """Custom exception for destination folder errors."""



class RepositoryFolderError(Exception):
    """Custom exception for errors related to folders in the repository."""

    def __init__(self, folder_path: str, repo_url: str, branch: str):
        super().__init__(
            f"The folder '{folder_path}' does not exist in the repository '{repo_url}' (branch: '{branch}')."
        )

# TODO: refactor
def scaffold_git_repo(
    repo_url: str,
    dest_folder: Optional[pl.Path] = None,
    folder_path: Optional[str] = None,
    checkout: Optional[str] = "main",
) -> None:
    """
    Downloads a specific folder from a Git repository without including the .git directory.
    If folder_path is not specified or is ".", the entire repository is downloaded.

    Args:
        repo_url (str): The URL of the Git repository.
        dest_folder (Optional[pl.Path]): The destination folder where the folder will be downloaded.
                                          Defaults to the current directory if None is passed.
        folder_path (Optional[str]): The path to the folder in the repository to download.
                                     If None or ".", download the entire repo.
        checkout (Optional[str]): The branch name to check out. Defaults to 'main'.

    Raises:
        DestinationFolderError: If the destination folder cannot be created or already exists as a non-directory.
        RepositoryFolderError: If the specified folder_path does not exist in the repository.

    Returns:
        None
    """
    checkout = checkout or "main"
    # Set dest_folder to current directory if None
    dest_folder_path = pl.Path(dest_folder) if dest_folder is not None else pl.Path(".")

    # Check if the destination folder already exists
    if dest_folder_path.exists() and not dest_folder_path.is_dir():
        raise DestinationFolderError(
            f"Error: The path '{dest_folder_path}' exists and is not a directory."
        )

    # Create destination folder if it doesn't exist
    try:
        dest_folder_path.mkdir(parents=True, exist_ok=True)
    except Exception as e:
        raise DestinationFolderError(
            f"Error: Failed to create the destination folder '{dest_folder_path}'. Reason: {str(e)}"
        )

    # Create a temporary directory for cloning
    with tempfile.TemporaryDirectory() as temp_dir:
        temp_path = pl.Path(temp_dir)

        # Clone the repository without checking out files
        subprocess.run(
            ["git", "clone", "--no-checkout", repo_url, str(temp_path)], check=True
        )

        # Check if we are downloading the entire repo
        if folder_path == ".":
            # Simply check out the specified branch
            subprocess.run(
                ["git", "-C", str(temp_path), "checkout", checkout], check=True
            )
        else:
            # Enable sparse checkout if folder_path is specified
            sparse_checkout_path = temp_path / ".git" / "info" / "sparse-checkout"

            with sparse_checkout_path.open("w") as sparse_file:
                sparse_file.write(folder_path + "\n")

            # Configure sparse checkout
            subprocess.run(
                [
                    "git",
                    "-C",
                    str(temp_path),
                    "config",
                    "core.sparseCheckout",
                    "true",
                ],
                check=True,
            )

            # Attempt to checkout the branch to validate the folder_path
            checkout_result = subprocess.run(
                ["git", "-C", str(temp_path), "checkout", checkout],
                stderr=subprocess.PIPE,
            )

            if checkout_result.returncode != 0:
                raise RuntimeError(
                    f"Error: Failed to checkout branch '{checkout}' from repository '{repo_url}'. "
                    f"Details: {checkout_result.stderr.decode().strip()}"
                )

            # Now check if the specified folder_path exists after checkout
            full_folder_path = temp_path / folder_path
            if not full_folder_path.exists():
                raise RepositoryFolderError(folder_path, repo_url, checkout)

        # Move contents to the destination folder
        for item in temp_path.iterdir():
            # Skip the .git directory
            if item.name == ".git":
                continue

            # Define the destination item path
            dest_item_path = dest_folder_path / item.name

            # Handle potential conflicts
            if dest_item_path.exists():
                # Use Typer's echo for logging instead of print
                typer.echo(f"Warning: {dest_item_path} already exists. Skipping.")
                continue

            # Move the item to the destination folder
            shutil.move(str(item), str(dest_folder_path))


# Example usage
if __name__ == "__main__":
    name, email = get_author_info()
    print(f"Author Name: {name}, Author Email: {email}")

    repo_url = "https://github.com/primefaces/primereact-examples.git"
    folder_path = "astro-basic-ts"
    dest_folder = "."
    branch_name = "main"
    scaffold_git_repo(
        repo_url=repo_url,
        dest_folder=dest_folder,
        folder_path=folder_path,
        checkout=branch_name,
    )
