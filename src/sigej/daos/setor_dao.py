from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.setor import Setor

class SetorDAO(BaseDAO):
    def insert(self, setor: Setor) -> int:
        return self._execute_returning_id(
            "INSERT INTO setor (nome, sigla) VALUES (%s, %s) RETURNING id",
            [setor.nome, setor.sigla],
        )

    def list_all(self) -> list[Setor]:
        rows = self._fetchall("SELECT id, nome, sigla FROM setor ORDER BY nome")
        return [Setor(*row) for row in rows]

    def find_by_id(self, setor_id: Optional[int]) -> Setor:
        row = self._fetchone("SELECT id, nome, sigla FROM setor WHERE id = %s", [setor_id])
        return Setor(*row) if row else None
