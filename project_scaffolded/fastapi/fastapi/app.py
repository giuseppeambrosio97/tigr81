import logging

import uvicorn
from fastapi import Depends, FastAPI

from fastapi import LOGGING_CONF_LOCATION, dependencies
from fastapi.config.model import API_CONFIG
from fastapi.routers import health


logger = logging.getLogger(__name__)

app = FastAPI(
    dependencies=[Depends(dependencies.get_apikey_header)],
)

app.include_router(health.router)

if __name__ == "__main__":
    uvicorn.run("app:app", 
        host=API_CONFIG.host, 
        port=API_CONFIG.port, 
        reload=API_CONFIG.reload,
        log_config=LOGGING_CONF_LOCATION.as_posix()
    )