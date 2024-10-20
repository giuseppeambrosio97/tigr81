from typing import Literal
from pydantic_settings import BaseSettings

EnvironmentType = Literal["default", "local", "dev", "prod"]


class AppSettings(BaseSettings):
    environment: EnvironmentType = "local"


APP_SETTINGS = AppSettings()
