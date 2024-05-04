import pathlib as pl
from typing import Dict, Optional, Union

import typer
from pydantic import BaseModel
import yaml

from tigr81 import DEFAULT_HUB_LOCATION
from tigr81.utils.read_yaml import read_yaml


class HubTemplate(BaseModel):
    name: str
    template: Union[str, pl.Path]
    checkout: Optional[str] = None
    directory: Optional[str] = None

    def __str__(self):
        name_str = f"template name: {self.name}"
        template_str = f"template location: {self.template}"
        checkout_str = f"checkout: {self.checkout}" if self.checkout else ""
        directory_str = f"directory: {self.directory}" if self.directory else ""
        return "\n".join([name_str, template_str, checkout_str, directory_str])

    @staticmethod
    def prompt() -> "HubTemplate":
        hub_template_name = typer.prompt(
            "Enter the template name", default="my-template"
        )
        template = typer.prompt("Enter the template location (git repo, local)")
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
        hub_templates_str = "\n".join(
            [f">>>\n{ht}" for ht in self.hub_templates.values()]
        )
        return f"""HUB INFO:
HUB NAME: {self.name}
HUB TEMPLATES:\n{hub_templates_str}
"""

    @staticmethod
    def from_yaml(path: pl.Path) -> "Hub":
        hub_dct = read_yaml(path)
        return Hub(**hub_dct)

    @staticmethod
    def prompt() -> "Hub":
        hub_name = typer.prompt("Enter the hub name", default="my-hub")

        hub_templates = {}

        while typer.confirm("Do you want to add a template? (y/n)", default=True):
            hub_template = HubTemplate.prompt()
            hub_templates[hub_template.name] = hub_template

        return Hub(name=hub_name, hub_templates=hub_templates)
