import logging
import atexit
from psycopg_pool import ConnectionPool
from src.sigej.config import Config

class Database:
    def __init__(self):
        self.__pool = ConnectionPool(conninfo=Config.Database.url())
        self.__load_schema()
        atexit.register(self.__pool.close)

    def connection(self):
        return self.__pool.connection()

    def __load_schema(self):
        schema_path = Config.Paths.SCRIPTS / "schema.sql"
        if not schema_path.exists():
            raise FileNotFoundError(f"Arquivo 'schema.sql' não encontrado no caminho: {schema_path}.")

        with open(schema_path, "r", encoding="utf-8") as file:
            schema_sql = file.read()

        with self.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(schema_sql)
                conn.commit()
        logging.info("Banco de dados inicializado com sucesso.")

database = Database()
