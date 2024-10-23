import pathlib as pl
import shutil
import subprocess
from typing import Optional, Tuple


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


def scaffold_git_repo(
    repo_url: str,
    dest_folder: str,
    folder_path: Optional[str] = None,
    checkout: Optional[str] = "main",
) -> None:
    """
    Downloads a specific folder from a Git repository without including the .git directory.
    If folder_path is not specified, the entire repository is downloaded.

    Args:
        repo_url (str): The URL of the Git repository.
        dest_folder (str): The destination folder where the folder will be downloaded.
        folder_path (Optional[str]): The path to the folder in the repository to download. If None, download the entire repo.
        checkout (Optional[str]): The branch name to check out. Defaults to 'main'.

    Returns:
        None
    """
    dest_folder_path = pl.Path(dest_folder)
    dest_folder_path.mkdir(parents=True, exist_ok=True)

    # Clone the repository without checking out files
    subprocess.run(
        ["git", "clone", "--no-checkout", repo_url, str(dest_folder_path)], check=True
    )

    if folder_path:
        # Enable sparse checkout if folder_path is specified
        sparse_checkout_path = dest_folder_path / ".git" / "info" / "sparse-checkout"

        with sparse_checkout_path.open("w") as sparse_file:
            sparse_file.write(folder_path + "\n")

        # Configure sparse checkout
        subprocess.run(
            [
                "git",
                "-C",
                dest_folder_path,
                "config",
                "core.sparseCheckout",
                "true",
            ],
            check=True,
        )

    # Checkout the specified folder or the entire repository
    subprocess.run(
        ["git", "-C", str(dest_folder_path), "checkout", checkout], check=True
    )

    # Remove the .git directory
    shutil.rmtree(dest_folder_path / ".git")


# Example usage
if __name__ == "__main__":
    # Retrieve author information
    name, email = get_author_info()
    print(f"Author Name: {name}, Author Email: {email}")

    # Example usage for downloading a folder from a Git repository
    repo_url = "https://github.com/primefaces/primereact-examples.git"
    folder_path = ""  # Folder you want to download
    dest_folder = "downloaded_folder"  # Destination folder
    branch_name = "main"  # Specify the branch you want to check out
    scaffold_git_repo(repo_url=repo_url, dest_folder=dest_folder, folder_path=folder_path, checkout=branch_name)
