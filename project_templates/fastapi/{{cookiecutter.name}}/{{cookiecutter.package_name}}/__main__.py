import uvicorn

from {{cookiecutter.package_name}} import LOGGING_CONF_LOCATION
from {{cookiecutter.package_name}}.config.model import API_CONFIG

if __name__ == '__main__':
    uvicorn.run(
        "{{cookiecutter.package_name}}.app:app",
        host=API_CONFIG.host,
        port=API_CONFIG.port,
        reload=API_CONFIG.reload,
        log_config=LOGGING_CONF_LOCATION.as_posix(),
    )