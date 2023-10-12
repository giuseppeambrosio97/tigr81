import os

from cookiecutter.main import cookiecutter
import typer

from tigr81 import REPO_LOCATION
from tigr81.commands.scaffold.project_template import (
    ProjectTemplate,
    ProjectTemplateOptions,
    ProjectTypeEnum
)

REPO_TEMPLATES = "https://github.com/giuseppeambrosio97/tigr81.git"


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
):
    """Scaffold a project template"""
    PROJECT_TEMPLATE_LOCATION = REPO_TEMPLATES
    checkout = "develop"

    if os.getenv("TIGR81_ENVIRONMENT") == "local":
        PROJECT_TEMPLATE_LOCATION = REPO_LOCATION.as_posix()
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
        output_dir=".",
        no_input=default,
        extra_context=project_template.project_options.model_dump(),
        checkout=checkout,
        directory=f"project_templates/{project_template.project_type}",
    )
