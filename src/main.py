from fastapi import FastAPI, Depends

from src.service.security import key_auth
from src.views.api import router

app = FastAPI()

app.include_router(router)


@app.get("/", dependencies=[Depends(key_auth)])
def read_root():
    return {"message": "Server is running."}
