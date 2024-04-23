from pydantic_settings import BaseSettings


class CliSettings(BaseSettings):
    tigr81_environment: str


CLI_SETTINGS = CliSettings()
