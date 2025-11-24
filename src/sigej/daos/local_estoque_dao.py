from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.local_estoque import LocalEstoque

class LocalEstoqueDAO(BaseDAO):
    def insert(self, local: LocalEstoque) -> int:
        return self._execute_returning_id(
            "INSERT INTO local_estoque (descricao, responsavel_id) VALUES (%s, %s) RETURNING id",
            [local.descricao, local.responsavel_id],
        )

    def list_all(self) -> list[LocalEstoque]:
        rows = self._fetchall("SELECT id, descricao, responsavel_id FROM local_estoque ORDER BY descricao")
        return [LocalEstoque(*row) for row in rows]

    def find_by_id(self, local_id: Optional[int]) -> LocalEstoque:
        row = self._fetchone("SELECT id, descricao, responsavel_id FROM local_estoque WHERE id = %s", [local_id])
        return LocalEstoque(*row) if row else None