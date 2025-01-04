import os
from dotenv import load_dotenv

from school_control_system_repository.config import DatabaseConfig

load_dotenv()

HOST = os.getenv("HOST", "")
USER_NAME = os.getenv("USER_NAME", "")
PASSWORD = os.getenv("PASSWORD", "")
DATABASE_NAME = os.getenv("DATABASE_NAME", "")

config = DatabaseConfig(
    HOST=HOST,
    USER_NAME=USER_NAME,
    PASSWORD=PASSWORD,
    DATABASE_NAME=DATABASE_NAME
)
