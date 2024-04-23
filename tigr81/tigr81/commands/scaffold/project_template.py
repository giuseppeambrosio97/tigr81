from enum import Enum
from typing import Dict, List, Optional
import click

from pydantic import BaseModel, EmailStr
import pathlib as pl

import typer

PROJECT_TEMPLATE_DEFAULT_RELATIVE_PATH = pl.Path(".")


class ProjectTypeEnum(str, Enum):
    FAST_API = "fastapi"
    POETRY_PKG = "poetry_pkg"
    PRIME_REACT = "prime-react"
    # GCP_CLOUD_FUNCTION = "gcp_cloud_function"
    # COOKIECUTTER = "cookiecutter"

    @staticmethod
    def get_monorepo_types() -> List["ProjectTypeEnum"]:
        return [ProjectTypeEnum.FAST_API, ProjectTypeEnum.POETRY_PKG]

    def __repr__(self) -> str:
        return self.value

    def __str__(self):
        return self.value


class ProjectTemplateOptions(BaseModel):
    name: str
    package_name: str
    description: str
    author_name: Optional[str] = "name surname"
    author_email: Optional[EmailStr] = "email@gmail.com"


    @classmethod
    def prompt(cls) -> "ProjectTemplateOptions":
        name = typer.prompt("Enter the project name", default="myproject")
        package_name = typer.prompt("Enter the package name for the project", default="myproject")
        description = typer.prompt("Enter a description for the project", default="A description for the project")
        author_name = typer.prompt("Enter the author name for the project", default="name surname")
        author_email = typer.prompt("Enter the author email for the project", default="email@gmail.com")

        return ProjectTemplateOptions(
            name=name,
            package_name=package_name,
            description=description,
            author_name=author_name,
            author_email=author_email
        )
        

class Dependency(BaseModel):
    name: str
    relative_path: Optional[pl.Path] = pl.Path(".")

    @classmethod
    def prompt(cls, available_dependencies: List["ProjectTemplate"]):
        names = [pt.project_options.name for pt in available_dependencies]
        name = typer.prompt("Enter the dependency name", type=click.Choice(names))

        selected_project_template = None
        for pt in available_dependencies:
            if pt.project_options.name == name:
                selected_project_template = pt
        
        if selected_project_template is None:
            raise ValueError("Invalid selected dependency..")
        

        # relative_path = typer.prompt("Enter the relative path of the dependency", default=pl.Path("."))

        return Dependency(
            name=name,
            relative_path=pl.Path("../") / selected_project_template.relative_path / selected_project_template.project_options.name
        )


class ProjectTemplate(BaseModel):
    project_type: ProjectTypeEnum
    relative_path: Optional[pl.Path] = PROJECT_TEMPLATE_DEFAULT_RELATIVE_PATH
    project_options: ProjectTemplateOptions
    dependencies: Optional[List[Dependency]] = []

    class Config:
        use_enum_values = True

    @property
    def extra_content(self) -> Dict:
        extra_content = self.project_options.model_dump(mode="json")

        extra_content["dependencies"] = {dependency.name: dependency.model_dump(mode="json") for dependency in self.dependencies}

        return extra_content
    
    @classmethod
    def prompt(cls, available_dependencies: List["ProjectTemplate"] = None) -> "ProjectTemplate":
        project_type = typer.prompt("Enter the project template type for the component you want to add", type=click.Choice(ProjectTypeEnum.get_monorepo_types()))

        relative_path = typer.prompt("Enter the relative path of the component you want to add", default=PROJECT_TEMPLATE_DEFAULT_RELATIVE_PATH)

        project_options = ProjectTemplateOptions.prompt()

        dependencies = []
        if available_dependencies:
            while typer.confirm("Do you want to add a dependency for this component? (y/n)", default=True):
                dependencies.append(Dependency.prompt(
                    available_dependencies=available_dependencies
                ))

        return ProjectTemplate(
            project_type=project_type,
            relative_path=relative_path,
            project_options=project_options,
            dependencies=dependencies
        )


if __name__ == "__main__":
    pt = ProjectTemplate.prompt()