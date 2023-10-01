import os
import pathlib as pl

__version__ = "1.0.0"

PACKAGE_LOCATION = pl.Path(os.path.dirname(__file__))
RESOURCES_LOCATION = PACKAGE_LOCATION / "resources"
CONFIG_LOCATION = RESOURCES_LOCATION / "config"
LOGGING_CONF_LOCATION = CONFIG_LOCATION / "logging.conf"
