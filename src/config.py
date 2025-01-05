import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
if SECRET_KEY == "":
    raise Exception("SECRET_KEY environment variable is not set")
ALGORITHM = os.getenv("ALGORITHM", "HS256")
DATABASE_URL = os.getenv("DATABASE_URL") or ""
if DATABASE_URL == "":
    raise Exception("DATABASE_URL environment variable is not set")

DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "False") == "True"
