from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.status_ordem_servico import StatusOrdemServico

class StatusOrdemServicoDAO(BaseDAO):
    def insert(self, status: StatusOrdemServico) -> int:
        return self._execute_returning_id(
            "INSERT INTO status_ordem_servico (descricao) VALUES (%s) RETURNING id", [status.descricao]
        )

    def list_all(self) -> list[StatusOrdemServico]:
        rows = self._fetchall("SELECT id, descricao FROM status_ordem_servico ORDER BY id")
        return [StatusOrdemServico(*row) for row in rows]

    def find_by_id(self, status_id: Optional[int]) -> StatusOrdemServico:
        row = self._fetchone("SELECT id, descricao FROM status_ordem_servico WHERE id = %s", [status_id])
        return StatusOrdemServico(*row) if row else None
