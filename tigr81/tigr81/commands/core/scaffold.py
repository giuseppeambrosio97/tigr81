import subprocess
from typing import List

import typer
from cookiecutter.main import cookiecutter
from tigr81 import LOCAL_REPO_LOCATION, REPO_LOCATION
from tigr81.cli_settings import CLI_SETTINGS
from tigr81.commands.scaffold.project_template import (
    ProjectTemplate,
    ProjectTemplateOptions,
    ProjectTypeEnum,
)
import pathlib as pl


def scaffold(
    project_type: ProjectTypeEnum,
    default: bool = False,
    output_dir: pl.Path = pl.Path("."),
):
    author_email = subprocess.run(
        ["git", "config", "user.email"], capture_output=True, text=True, check=True
    ).stdout.strip()
    author_name = author_email.split("@")[0]

    project_template = ProjectTemplate(
        project_type=project_type,
        project_options=ProjectTemplateOptions(
            name=project_type,
            package_name=project_type,
            description=project_type,
            author_name=author_name,
            author_email=author_email,
        ),
    )

    scaffold_project_template(project_template, default=default, output_dir=output_dir)


def scaffold_project_template(
    project_template: ProjectTemplate,
    default: bool = False,
    output_dir: pl.Path = pl.Path("."),
):
    __PROJECT_TEMPLATE_LOCATION = REPO_LOCATION
    checkout = "develop"

    if CLI_SETTINGS.tigr81_environment == "local":
        __PROJECT_TEMPLATE_LOCATION = LOCAL_REPO_LOCATION.as_posix()
        checkout = None

    typer.echo(
        f"Scaffolding a {project_template.project_type} project template from {__PROJECT_TEMPLATE_LOCATION}"
    )

    cookiecutter(
        template=__PROJECT_TEMPLATE_LOCATION,
        output_dir=output_dir,
        no_input=default,
        extra_context=project_template.extra_content,
        checkout=checkout,
        directory=f"project_templates/{project_template.project_type}",
    )


def scaffold_cookiecutter(
    project_type: ProjectTypeEnum, output_dir: pl.Path = pl.Path(".")
):
    __PROJECT_TEMPLATE_LOCATION = REPO_LOCATION
    checkout = "develop"

    if CLI_SETTINGS.tigr81_environment == "local":
        __PROJECT_TEMPLATE_LOCATION = LOCAL_REPO_LOCATION.as_posix()
    typer.echo(
        f"Scaffolding a {project_type} project template from {__PROJECT_TEMPLATE_LOCATION}"
    )

    cookiecutter(
        template=__PROJECT_TEMPLATE_LOCATION,
        output_dir=output_dir,
        no_input=False,
        checkout=checkout,
        directory=f"project_templates/{project_type}",
    )



def scaffold_monorepo(components: List[ProjectTemplate]):
    pass
