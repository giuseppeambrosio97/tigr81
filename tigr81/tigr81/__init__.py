import pathlib as pl

__version__ = "1.1.2"

PACKAGE_LOCATION = pl.Path(__file__).parent.resolve()
ROOT_LOCATION = PACKAGE_LOCATION.parent
LOCAL_REPO_LOCATION = ROOT_LOCATION.parent

LOCAL_PROJECT_TEMPLATES_FOLDER_LOCATION = LOCAL_REPO_LOCATION / "project_templates"
RESOURCE_LOCATION = PACKAGE_LOCATION / "resources"


PYPY_URL = "https://pypi.org/project/tigr81/"
REPO_LOCATION = "https://github.com/giuseppeambrosio97/tigr81.git"
