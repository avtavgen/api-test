import os

from dotenv import load_dotenv
from fastapi import FastAPI
from src.views.views import router

load_dotenv('.env')

DATABASE_URL = os.environ.get("DATABASE_URL")

app = FastAPI()

app.include_router(router)


@app.get("/")
def read_root():
    return {"message": "Server is running."}
