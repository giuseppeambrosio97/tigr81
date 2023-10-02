import os

from cookiecutter.main import cookiecutter
import typer

from tigr81 import LOCAL_PROJECT_TEMPLATES_FOLDER_LOCATION
from tigr81.commands.models import (
    Author,
    ProjectTemplate,
    ProjectTemplateOptions,
    ProjectTypeEnum
)

REPO_TEMPLATES = "git@github.com:giuseppeambrosio97/tigr81.git"


app = typer.Typer()


@app.callback()
def callback():
    """
    Scaffold a project template
    """


@app.command()
def scaffold(
    project_type: ProjectTypeEnum,
    default: bool = typer.Option(
        False, help="Set to False to enable input during cookiecutter execution"
    ),
):
    """Scaffold a FAST API project"""
    PROJECT_TEMPLATE_LOCATION = REPO_TEMPLATES

    if os.getenv("TIGR81_ENVIRONMENT") == "local":
        PROJECT_TEMPLATE_LOCATION = LOCAL_PROJECT_TEMPLATES_FOLDER_LOCATION.as_posix()

    typer.echo(
        f"Scaffolding a {project_type} project template from {PROJECT_TEMPLATE_LOCATION}"
    )

    project_template = ProjectTemplate(
        type=project_type,
        project_options=ProjectTemplateOptions(
            name="fastapi-app",
            package_name="fastapi_pkg",
            description="FAST API web app",
            author=Author(name="author name", email="authornemail@gmail.com")
        )
    )

    cookiecutter(
        template=PROJECT_TEMPLATE_LOCATION,
        output_dir=".",
        no_input=default,
        extra_context=project_template.project_options.model_dump(),
        # checkout="feat/scaffolder",
        directory=project_template.type,
    )
