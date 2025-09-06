from fastapi import Depends, APIRouter

from src.db.models import UserRequest, UserResponse
from src.service.logger_config import get_logger
from src.service.security import key_auth

logger = get_logger(__name__)

router = APIRouter(
    prefix="/api",
)


@router.post("/", dependencies=[Depends(key_auth)], response_model=UserResponse)
async def get_user(request: UserRequest):
    logger.debug(f"Received request: {request}")
    return user
