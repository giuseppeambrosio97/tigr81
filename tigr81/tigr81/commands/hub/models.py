import os
import pathlib as pl
from typing import Dict, Optional, Union

import typer
import yaml
from pydantic import BaseModel

import tigr81.utils as tigr81_utils


def _extract_template_name(template: str) -> str:
    """
    Extracts the name of the template from either a local file path or a remote URL.

    For local paths, it returns the last directory or file name. For remote Git URLs,
    it extracts the repository name from the URL by splitting on '.' and taking the first part.

    Args:
        template (str): The template location, which can be a local file path (Linux, MacOS, Windows)
                        or a remote URL (e.g., a Git repository URL).

    Returns:
        str: The extracted template name, which is the last part of the local path or the remote URL.
             - For local paths, it's the last folder or file name.
             - For remote URLs, it's the last part of the URL, typically the repository name,
               with any extensions removed.

    Example:
        - Input: "/home/user/projects/my-template" -> Output: "my-template"
        - Input: "https://github.com/user/my-repo.git" -> Output: "my-repo"
    """
    path = pl.Path(template)
    
    if path.is_absolute() or os.path.exists(template):
        return path.name
    else:
        template_name = template.rstrip("/").split("/")[-1]
        return template_name.split(".")[0]



class HubTemplate(BaseModel):
    name: str
    template: Union[str, pl.Path]
    checkout: Optional[str] = None
    directory: Optional[str] = None

    def __str__(self):
        components = [
            f"\tTemplate name: {self.name}",
            f"\tTemplate location: {self.template}",
        ]
        if self.checkout:
            components.append(f"\tCheckout: {self.checkout}")
        if self.directory:
            components.append(f"\tDirectory: {self.directory}\n")
        return "\n".join(components)

    @staticmethod
    def prompt() -> "HubTemplate":
        template = typer.prompt("Enter the template location (git repo, local)")

        hub_template_name = _extract_template_name(template)
        hub_template_name = typer.prompt(
            "Enter the template name", default=hub_template_name
        )

        template_pl = pl.Path(template)
        checkout = None
        directory = None
        if not template_pl.exists() or not template_pl.is_dir():
            checkout = typer.prompt(
                "Enter the checkout (only needed for remote template)",
                default="develop",
            )
            directory = typer.prompt(
                "Enter the relative path to a template in a repository (only needed for remote template)",
                default=pl.Path("."),
            )

        return HubTemplate(
            name=hub_template_name,
            template=template,
            checkout=checkout,
            directory=directory,
        )


class Hub(BaseModel):
    name: str
    hub_templates: Dict[str, HubTemplate]

    def to_yaml(self, folder_path: pl.Path) -> None:
        path = folder_path / f"{self.name}.yml"
        with open(path, "w") as f:
            yaml.dump(
                data=self.model_dump(mode="json"),
                stream=f,
            )

    def __str__(self):
        hub_templates_str = "".join([f"{ht}" for ht in self.hub_templates.values()])
        return f"""Hub info
hub name: {self.name}
hub templates:\n\n{hub_templates_str}
"""

    @staticmethod
    def from_yaml(path: pl.Path) -> "Hub":
        hub_dct = tigr81_utils.read_yaml(path)
        return Hub(**hub_dct)

    @staticmethod
    def prompt() -> "Hub":
        hub_name = typer.prompt("Enter the hub name", default="my-hub")

        hub_templates = {}

        while typer.confirm("Do you want to add a template? (y/n)", default=True):
            hub_template = HubTemplate.prompt()
            hub_templates[hub_template.name] = hub_template

        return Hub(name=hub_name, hub_templates=hub_templates)
