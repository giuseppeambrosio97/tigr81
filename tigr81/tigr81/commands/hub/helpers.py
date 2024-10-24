import pathlib as pl
from typing import Dict, List

import typer

from tigr81 import AVAILABLE_HUBS
from tigr81.commands.hub.models import Hub, HubTemplate


def load_hubs(hub_folders: List[pl.Path] = AVAILABLE_HUBS) -> Dict[str, Hub]:
    hubs = {}
    for hub_folder in hub_folders:
        for hub_path in hub_folder.glob("*.yml"):
            hub = Hub.from_yaml(hub_path)
            hubs[hub.name] = hub
    return hubs


def is_hub_name_valid(
    hub_name: str, hub_folders: List[pl.Path] = AVAILABLE_HUBS
) -> bool:
    hubs = load_hubs(hub_folders)
    return hub_name not in hubs


def get_template_from_hubs(
    hub_name: str, template_name: str, hubs: Dict[str, Hub]
) -> HubTemplate:
    hub = hubs.get(hub_name)
    if not hub:
        typer.echo(f"Hub name not found: {hub_name}")
        raise typer.Exit()

    template = hub.hub_templates.get(template_name)

    if not template:
        typer.echo(f"Hub template {template_name} not found in hub {hub_name}")
        raise typer.Exit()

    return template
