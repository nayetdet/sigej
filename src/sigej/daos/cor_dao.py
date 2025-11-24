from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.cor import Cor

class CorDAO(BaseDAO):
    def insert(self, cor: Cor) -> int:
        return self._execute_returning_id("INSERT INTO cor (nome) VALUES (%s) RETURNING id", [cor.nome])

    def list_all(self) -> list[Cor]:
        rows = self._fetchall("SELECT id, nome FROM cor ORDER BY nome")
        return [Cor(*row) for row in rows]

    def find_by_id(self, cor_id: int) -> Cor:
        row = self._fetchone("SELECT id, nome FROM cor WHERE id = %s", [cor_id])
        return Cor(*row) if row else None
