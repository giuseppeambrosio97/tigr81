from dataclasses import dataclass

from {{cookiecutter.package_name}}.config.loading import config

@dataclass(frozen=True)
class ApiConfig:
    host: str
    port: int
    reload: bool


API_CONFIG = ApiConfig(**config["api_config"])