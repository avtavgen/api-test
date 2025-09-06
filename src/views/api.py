from fastapi import Depends, APIRouter, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from starlette.responses import JSONResponse

from src.db.core import get_session
from src.db.models import User, UserCreate
from src.service.logger_config import get_logger
from src.service.security import key_auth

logger = get_logger(__name__)

router = APIRouter(
    prefix="/api",
)


@router.get("/users", response_model=list[User], dependencies=[Depends(key_auth)])
async def get_users(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(User))
    return result.scalars().all()


@router.post("/user", dependencies=[Depends(key_auth)])
async def add_user(new_user: UserCreate, session: AsyncSession = Depends(get_session)):
    new_user = User(name=new_user.name, email=new_user.email, password=new_user.password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return JSONResponse(
        content={"message": "User created!"},
        status_code=status.HTTP_201_CREATED
    )
