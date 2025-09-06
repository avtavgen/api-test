import os


LOGGING_LEVEL = os.getenv("LOGGING_LEVEL", default="INFO")
AUTH_TOKEN = os.getenv("AUTH_TOKEN", default="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9")
DATABASE_URL = os.environ.get("DATABASE_URL", default="sqlite+aiosqlite:///test.db")
