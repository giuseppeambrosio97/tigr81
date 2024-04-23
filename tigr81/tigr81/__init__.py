import pathlib as pl

__version__ = "1.1.0"

PACKAGE_LOCATION = pl.Path(__file__).parent.resolve()
ROOT_LOCATION = PACKAGE_LOCATION.parent
LOCAL_REPO_LOCATION = ROOT_LOCATION.parent

LOCAL_PROJECT_TEMPLATES_FOLDER_LOCATION = LOCAL_REPO_LOCATION / "project_templates"
RESOURCE_LOCATION = PACKAGE_LOCATION / "resources"


REPO_LOCATION = "https://github.com/giuseppeambrosio97/tigr81.git"
