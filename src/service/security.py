from fastapi import Depends, HTTPException, status, Security
from fastapi.security import APIKeyHeader

from src.settings import AUTH_TOKEN


def key_sec(apikey_header: str = Security(APIKeyHeader(name="X-API-Key", auto_error=False))):
    if not apikey_header or not AUTH_TOKEN:
        return None
    return apikey_header == AUTH_TOKEN


async def key_auth(api_key: str = Depends(key_sec)):
    if not api_key:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authenticated")
