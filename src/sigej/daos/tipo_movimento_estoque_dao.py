from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.tipo_movimento_estoque import TipoMovimentoEstoque

class TipoMovimentoEstoqueDAO(BaseDAO):
    def insert(self, tipo: TipoMovimentoEstoque) -> int:
        return self._execute_returning_id(
            "INSERT INTO tipo_movimento_estoque (descricao, sinal) VALUES (%s, %s) RETURNING id",
            [tipo.descricao, tipo.sinal],
        )

    def list_all(self) -> list[TipoMovimentoEstoque]:
        rows = self._fetchall("SELECT id, descricao, sinal FROM tipo_movimento_estoque ORDER BY id")
        return [TipoMovimentoEstoque(*row) for row in rows]

    def find_by_id(self, tipo_id: Optional[int]) -> TipoMovimentoEstoque:
        row = self._fetchone("SELECT id, descricao, sinal FROM tipo_movimento_estoque WHERE id = %s", [tipo_id])
        return TipoMovimentoEstoque(*row) if row else None
