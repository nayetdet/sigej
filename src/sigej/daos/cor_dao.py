from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.cor import Cor

class CorDAO(BaseDAO):
    def insert(self, cor: Cor) -> int:
        return self._execute_returning_id("INSERT INTO cor (nome) VALUES (%s) RETURNING id", [cor.nome])

    def list_all(self) -> list[Cor]:
        rows = self._fetchall("SELECT id, nome FROM cor ORDER BY nome")
        return [Cor(*row) for row in rows]
