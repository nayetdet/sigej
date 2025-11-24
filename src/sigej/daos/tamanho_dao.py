from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.tamanho import Tamanho

class TamanhoDAO(BaseDAO):
    def insert(self, tamanho: Tamanho) -> int:
        return self._execute_returning_id(
            "INSERT INTO tamanho (descricao) VALUES (%s) RETURNING id",
            [tamanho.descricao],
        )

    def list_all(self) -> list[Tamanho]:
        rows = self._fetchall("SELECT id, descricao FROM tamanho ORDER BY descricao")
        return [Tamanho(*row) for row in rows]

    def find_by_id(self, tamanho_id: int) -> Tamanho:
        row = self._fetchone("SELECT id, descricao FROM tamanho WHERE id = %s", [tamanho_id])
        return Tamanho(*row) if row else None
