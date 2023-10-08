import pathlib as pl
import os

__version__ = "1.0.0"

PACKAGE_LOCATION = pl.Path(os.path.dirname(__file__))
ROOT_LOCATION = PACKAGE_LOCATION.parent
REPO_LOCATION = ROOT_LOCATION.parent

LOCAL_PROJECT_TEMPLATES_FOLDER_LOCATION = REPO_LOCATION / "project_templates"
RESOURCE_LOCATION = PACKAGE_LOCATION / "resources"
