from enum import Enum
from pydantic_settings import BaseSettings

class EnvironmentEnum(str, Enum):
    DEFAULT = "default"
    LOCAL = "local"
    DEV = "dev"
    PROD = "prod"


class AppSettings(BaseSettings):
    environment: EnvironmentEnum = EnvironmentEnum.LOCAL

APP_SETTINGS = AppSettings()