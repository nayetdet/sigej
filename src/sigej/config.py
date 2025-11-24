from os import getenv
from pathlib import Path

class Config:
    class Flask:
        SECRET_KEY = getenv("FLASK_SECRET_KEY")

    class Database:
        HOST = getenv("DATABASE_HOST")
        PORT = getenv("DATABASE_PORT")
        NAME = getenv("DATABASE_NAME")
        USERNAME = getenv("DATABASE_USERNAME")
        PASSWORD = getenv("DATABASE_PASSWORD")

        @classmethod
        def url(cls):
            return f"dbname={cls.NAME} user={cls.USERNAME} password={cls.PASSWORD} host={cls.HOST} port={cls.PORT}"

    class Paths:
        ROOT: Path = Path(__file__).resolve().parents[2]
        SCRIPTS: Path = ROOT / "scripts"
