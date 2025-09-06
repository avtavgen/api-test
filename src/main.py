from contextlib import asynccontextmanager

from dotenv import load_dotenv
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel

from src.db.core import engine
from src.service.security import key_auth
from src.views.api import router

load_dotenv('.env')

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(lifespan=lifespan)

app.include_router(router)


@app.get("/", dependencies=[Depends(key_auth)])
def read_root():
    return {"message": "Server is running."}
