import uvicorn

from fastapi_app import LOGGING_CONF_LOCATION
from fastapi_app.config.model import API_CONFIG

if __name__ == '__main__':
    uvicorn.run(
        "fastapi_app.app:app",
        host=API_CONFIG.host,
        port=API_CONFIG.port,
        reload=API_CONFIG.reload,
        log_config=LOGGING_CONF_LOCATION.as_posix(),
    )