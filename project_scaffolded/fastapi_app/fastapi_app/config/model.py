from dataclasses import dataclass

from fastapi_app.config.loading import config

@dataclass(frozen=True)
class ApiConfig:
    host: str
    port: int
    reload: bool


API_CONFIG = ApiConfig(**config["api_config"])