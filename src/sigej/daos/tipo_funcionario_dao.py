from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.tipo_funcionario import TipoFuncionario

class TipoFuncionarioDAO(BaseDAO):
    def insert(self, tipo: TipoFuncionario) -> int:
        return self._execute_returning_id(
            "INSERT INTO tipo_funcionario (descricao) VALUES (%s) RETURNING id",
            [tipo.descricao],
        )

    def list_all(self) -> list[TipoFuncionario]:
        rows = self._fetchall("SELECT id, descricao FROM tipo_funcionario ORDER BY id")
        return [TipoFuncionario(*row) for row in rows]

    def find_by_id(self, tipo_id: Optional[int]) -> TipoFuncionario:
        row = self._fetchone("SELECT id, descricao FROM tipo_funcionario WHERE id = %s", [tipo_id])
        return TipoFuncionario(*row) if row else None