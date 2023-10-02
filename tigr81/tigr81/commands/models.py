from enum import Enum

from pydantic import BaseModel, EmailStr


class ProjectTypeEnum(str, Enum):
    FAST_API = "fastapi"
    # GCP_CLOUD_FUNCTION = "gcp_cloud_function"
    # COOKIECUTTER = "cookiecutter"
    # POETRY = "poetry"
    # MONO_REPO = "mono_repo"

    def __str__(self):
        return self.value

class Author(BaseModel):
    name: str
    email: EmailStr


class ProjectTemplateOptions(BaseModel):
    name: str
    package_name: str
    description: str
    author: Author


class ProjectTemplate(BaseModel):
    type: ProjectTypeEnum
    project_options: ProjectTemplateOptions

    class Config:
        use_enum_values = True