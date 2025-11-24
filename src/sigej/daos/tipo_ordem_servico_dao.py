from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.tipo_ordem_servico import TipoOrdemServico

class TipoOrdemServicoDAO(BaseDAO):
    def insert(self, tipo: TipoOrdemServico) -> int:
        return self._execute_returning_id(
            "INSERT INTO tipo_ordem_servico (descricao) VALUES (%s) RETURNING id", [tipo.descricao]
        )

    def list_all(self) -> list[TipoOrdemServico]:
        rows = self._fetchall("SELECT id, descricao FROM tipo_ordem_servico ORDER BY descricao")
        return [TipoOrdemServico(*row) for row in rows]

    def find_by_id(self, tipo_id: Optional[int]) -> TipoOrdemServico:
        row = self._fetchone("SELECT id, descricao FROM tipo_ordem_servico WHERE id = %s", [tipo_id])
        return TipoOrdemServico(*row) if row else None
