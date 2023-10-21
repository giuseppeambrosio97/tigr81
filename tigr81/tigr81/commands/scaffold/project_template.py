from enum import Enum
from typing import Dict, List, Optional

from pydantic import BaseModel, EmailStr
import pathlib as pl


class ProjectTypeEnum(str, Enum):
    FAST_API = "fastapi"
    POETRY_PKG = "poetry_pkg"
    # GCP_CLOUD_FUNCTION = "gcp_cloud_function"
    # COOKIECUTTER = "cookiecutter"
    # MONO_REPO = "mono_repo"

    def __str__(self):
        return self.value


class ProjectTemplateOptions(BaseModel):
    name: str
    package_name: str
    description: str
    author_name: Optional[str] = "name surname"
    author_email: Optional[EmailStr] = "email@gmail.com"


class Dependency(BaseModel):
    name: str
    relative_path: Optional[pl.Path] = pl.Path(".")


class ProjectTemplate(BaseModel):
    project_type: ProjectTypeEnum
    relative_path: Optional[pl.Path] = pl.Path(".")
    project_options: ProjectTemplateOptions
    dependencies: Optional[List[Dependency]] = []

    class Config:
        use_enum_values = True

    @property
    def extra_content(self) -> Dict:
        extra_content = self.project_options.model_dump(mode="json")

        extra_content["dependencies"] = {dependency.name: dependency.model_dump(mode="json") for dependency in self.dependencies}

        return extra_content
