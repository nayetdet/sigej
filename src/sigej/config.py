from os import getenv
from pathlib import Path

class Config:
    class Flask:
        SECRET_KEY: str = getenv("FLASK_SECRET_KEY")

    class Database:
        HOST: str = getenv("DATABASE_HOST")
        PORT: str = getenv("DATABASE_PORT")
        NAME: str = getenv("DATABASE_NAME")
        USERNAME: str = getenv("DATABASE_USERNAME")
        PASSWORD: str = getenv("DATABASE_PASSWORD")

        @classmethod
        def url(cls) -> str:
            return f"dbname={cls.NAME} user={cls.USERNAME} password={cls.PASSWORD} host={cls.HOST} port={cls.PORT}"

    class Paths:
        ROOT: Path = Path(__file__).resolve().parents[2]
        RESOURCES: Path = ROOT / "resources"
        RESOURCES_STATIC: Path = RESOURCES / "static"
        RESOURCES_STATIC_CSS: Path = RESOURCES_STATIC / "css"
        RESOURCES_TEMPLATES: Path = RESOURCES_STATIC / "templates"
        SCRIPTS: Path = ROOT / "scripts"
        SCRIPTS_SQL: Path = SCRIPTS / "sql"
