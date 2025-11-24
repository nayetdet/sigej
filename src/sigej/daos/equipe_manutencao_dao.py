from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.equipe_manutencao import EquipeManutencao

class EquipeManutencaoDAO(BaseDAO):
    def insert(self, equipe: EquipeManutencao) -> int:
        return self._execute_returning_id(
            "INSERT INTO equipe_manutencao (nome, turno) VALUES (%s, %s) RETURNING id",
            [equipe.nome, equipe.turno],
        )

    def list_all(self) -> list[EquipeManutencao]:
        rows = self._fetchall("SELECT id, nome, turno FROM equipe_manutencao ORDER BY nome")
        return [EquipeManutencao(*row) for row in rows]

    def find_by_id(self, equipe_id: Optional[int]) -> EquipeManutencao:
        row = self._fetchone("SELECT id, nome, turno FROM equipe_manutencao WHERE id = %s", [equipe_id])
        return EquipeManutencao(*row) if row else None