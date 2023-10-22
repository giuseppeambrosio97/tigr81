import os
from typing_extensions import Annotated

from cookiecutter.main import cookiecutter
import typer

from tigr81 import LOCAL_REPO_LOCATION, REPO_LOCATION
from tigr81.commands.monorepo import MANIFEST_FILE_NAME
from tigr81.commands.monorepo.manifest import Manifest

import pathlib as pl

from tigr81.utils.read_yaml import read_yaml


app = typer.Typer()


@app.callback()
def callback():
    """
    Handle monorepo project
    """


@app.command()
def add():
    """Add a component to the monorepo project"""
    typer.echo("Adding a component to the monorepo project")


@app.command()
def init(
    name: Annotated[str, typer.Argument(help="The name of the monorepo project")],
    relative_path: Annotated[str, typer.Argument(help="The folder in which the monorepo source code will be located")] = pl.Path("src"),
):
    """Initialize a monorepo project"""
    typer.echo("Inizializing a monorepo project")

    manifest_path = pl.Path(MANIFEST_FILE_NAME)

    if manifest_path.exists():
        overwrite = typer.confirm("The manifest file already exists, do you want to overwrite?")
        if not overwrite:
            typer.echo("Manifest file not overwritten!!")
            return 
        
    manifest = Manifest(
        name=name,
        relative_path=relative_path
    )
    typer.echo("Creating manifest file...")
    manifest.to_yaml()


@app.command()
def install():
    """Install every component inside the monorepo project"""
    typer.echo("Installing all the components of the monorepo project")


@app.command()
def remove():
    """Remove a component from the monorepo project"""
    typer.echo("Removing a component to the monorepo project")


@app.command()
def scaffold():
    """Scaffold a monorepo project"""
    #TODO: check if the file exists and add a method from_yaml in Manifest
    manifest_dct = read_yaml(MANIFEST_FILE_NAME)  

    manifest = Manifest(**manifest_dct)

    PROJECT_TEMPLATE_LOCATION = REPO_LOCATION
    checkout = "develop"

    if os.getenv("TIGR81_ENVIRONMENT") == "local":
        PROJECT_TEMPLATE_LOCATION = LOCAL_REPO_LOCATION.as_posix()
        checkout = None

    typer.echo(
        f"Scaffolding a monorepo project from {pl.Path.cwd() / MANIFEST_FILE_NAME}"
    )

    for component in manifest.components:
        typer.echo(f"Scaffolding {manifest.relative_path / component.relative_path / component.project_options.name} component...")
        cookiecutter(
            template=PROJECT_TEMPLATE_LOCATION,
            output_dir=manifest.relative_path / component.relative_path,
            no_input=True,
            extra_context=component.extra_content,
            checkout=checkout,
            directory=f"project_templates/{component.project_type}",
        ) 