from contextlib import contextmanager
from typing import Optional, Any, Iterable
from src.sigej.database import database

class BaseDAO:
    def __init__(self):
        self._database = database

    def _connection(self):
        return self._database.connection()

    @contextmanager
    def _cursor(self, conn=None):
        if conn is not None:
            cur = conn.cursor()
            try:
                yield cur
            finally:
                cur.close()
        else:
            with self._database.connection() as own_conn:
                with own_conn.cursor() as cur:
                    yield cur
                own_conn.commit()

    def _fetchone(self, sql: str, params: Optional[Iterable[Any]] = None, conn=None):
        with self._cursor(conn) as cur:
            cur.execute(sql, params or [])
            return cur.fetchone()

    def _fetchall(self, sql: str, params: Optional[Iterable[Any]] = None, conn=None):
        with self._cursor(conn) as cur:
            cur.execute(sql, params or [])
            return cur.fetchall()

    def _execute(self, sql: str, params: Optional[Iterable[Any]] = None, conn=None):
        with self._cursor(conn) as cur:
            cur.execute(sql, params or [])

    def _execute_returning_id(self, sql: str, params: Optional[Iterable[Any]] = None, conn=None) -> int:
        with self._cursor(conn) as cur:
            cur.execute(sql, params or [])
            new_id = cur.fetchone()[0]
        return new_id