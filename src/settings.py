import os

from dotenv import load_dotenv


load_dotenv('.env')

AUTH_TOKEN = os.getenv("AUTH_TOKEN")
LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", default="INFO")
DATABASE_URL = os.environ.get("DATABASE_URL", default="sqlite+aiosqlite:///test.db")
