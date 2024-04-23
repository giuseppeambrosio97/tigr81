import logging

from fastapi import Depends, FastAPI

from fastapi_app import dependencies
from fastapi_app.routers import health
from fastapi.middleware.cors import CORSMiddleware

logger = logging.getLogger(__name__)

app = FastAPI(
    dependencies=[Depends(dependencies.get_apikey_header)],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health.router)
