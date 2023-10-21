import os

from cookiecutter.main import cookiecutter
import typer

from tigr81 import LOCAL_REPO_LOCATION, REPO_LOCATION
from tigr81.commands.scaffold import manifest
from tigr81.commands.scaffold.manifest import Manifest
from tigr81.commands.scaffold.project_template import (
    Dependency,
    ProjectTemplate,
    ProjectTemplateOptions,
    ProjectTypeEnum
)

import pathlib as pl

from tigr81.utils.read_yaml import read_yaml


app = typer.Typer()


@app.callback()
def callback():
    """
    Scaffold project templates
    """


@app.command()
def scaffold(
    project_type: ProjectTypeEnum,
    default: bool = typer.Option(
        False, help="Set to False to enable input during cookiecutter execution"
    ),
    output_dir: pl.Path = typer.Option(
        pl.Path("."), help="Set if you want to scaffold the project template in a specific directory"
    )
):
    """Scaffold a project template"""
    PROJECT_TEMPLATE_LOCATION = REPO_LOCATION
    checkout = "develop"

    if os.getenv("TIGR81_ENVIRONMENT") == "local":
        PROJECT_TEMPLATE_LOCATION = LOCAL_REPO_LOCATION.as_posix()
        checkout = None

    typer.echo(
        f"Scaffolding a {project_type} project template from {PROJECT_TEMPLATE_LOCATION}"
    )

    project_template = ProjectTemplate(
        project_type=project_type,
        project_options=ProjectTemplateOptions(
            name=project_type,
            package_name=project_type,
            description=project_type,
        )
    )

    cookiecutter(
        template=PROJECT_TEMPLATE_LOCATION,
        output_dir=output_dir,
        no_input=default,
        extra_context=project_template.extra_content,
        checkout=checkout,
        directory=f"project_templates/{project_template.project_type}",
    )


MANIFEST_FILE_NAME = "manifest.yml"

@app.command("monorepo")
def scaffold_monorepo():
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

if __name__ == "__main__":
    project_type = "fastapi"
    PROJECT_TEMPLATE_LOCATION = REPO_LOCATION
    checkout = "develop"

    if os.getenv("TIGR81_ENVIRONMENT") == "local":
        PROJECT_TEMPLATE_LOCATION = LOCAL_REPO_LOCATION.as_posix()
        checkout = None

    typer.echo(
        f"Scaffolding a {project_type} project template from {PROJECT_TEMPLATE_LOCATION}"
    )

    project_template = ProjectTemplate(
        project_type=project_type,
        project_options=ProjectTemplateOptions(
            name=project_type,
            package_name=project_type,
            description=project_type,
        ),
        dependencies=[
            Dependency(name="dagprep", relative_path="../../dagprep"),
            Dependency(name="fresko", relative_path="../../fresko"),
        ]
    )

    # extra_content = project_template.project_options.momdel_dump()
    # extra_content["dependencies"] = {
    #     {"name": "pippo", "version": "1.1.1"},
    #     {"name": "fresko", "version": "2.2.2"}
    # }

    print(project_template.extra_content)

    cookiecutter(
        template=PROJECT_TEMPLATE_LOCATION,
        output_dir=".",
        no_input=True,
        # extra_context=project_template.project_options.model_dump(),
        extra_context=project_template.extra_content,
        checkout=checkout,
        directory=f"project_templates/{project_template.project_type}",
    )