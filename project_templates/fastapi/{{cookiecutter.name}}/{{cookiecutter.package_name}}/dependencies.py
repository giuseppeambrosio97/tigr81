import logging
import os
import secrets

from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

logger = logging.getLogger(__name__)

api_key_header = APIKeyHeader(name="X-API-Key")


async def get_apikey_header(apikey: str = Security(api_key_header)):
    """
        This function checks whether a request has the correct apikey.

    Args:
        apikey (str, optional): apikey taken from the header of the http request. Defaults to Header(...).

    Raises:
        HTTPException: The function raise an exception if the apikey is incorrect.
    """
    logger.info("apikey authentication in progress")
    if not secrets.compare_digest(apikey, os.getenv("API_KEY")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or missing API Key",
        )
