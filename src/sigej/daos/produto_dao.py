from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.produto import Produto

class ProdutoDAO(BaseDAO):
    def insert(self, produto: Produto) -> int:
        sql = """
        INSERT INTO produto (descricao, categoria_id, unidade_medida_id, marca_id)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """
        return self._execute_returning_id(
            sql, [produto.descricao, produto.categoria_id, produto.unidade_medida_id, produto.marca_id]
        )

    def find_by_id(self, produto_id: Optional[int]) -> Produto:
        row = self._fetchone(
            "SELECT id, descricao, categoria_id, unidade_medida_id, marca_id FROM produto WHERE id = %s",
            [produto_id],
        )
        return Produto(*row) if row else None

    def list_all(self) -> list[Produto]:
        rows = self._fetchall(
            "SELECT id, descricao, categoria_id, unidade_medida_id, marca_id FROM produto ORDER BY descricao"
        )
        return [Produto(*row) for row in rows]