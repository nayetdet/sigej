from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.produto_variacao import ProdutoVariacao

class ProdutoVariacaoDAO(BaseDAO):
    def insert(self, variacao: ProdutoVariacao) -> int:
        sql = """
        INSERT INTO produto_variacao (produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """
        return self._execute_returning_id(
            sql,
            [
                variacao.produto_id,
                variacao.cor_id,
                variacao.tamanho_id,
                variacao.codigo_barras,
                variacao.codigo_interno,
            ],
        )

    def find_by_id(self, variacao_id: Optional[int]) -> ProdutoVariacao:
        row = self._fetchone(
            """
            SELECT id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno
            FROM produto_variacao WHERE id = %s
            """,
            [variacao_id],
        )
        return ProdutoVariacao(*row) if row else None

    def list_by_produto(self, produto_id: int) -> list[ProdutoVariacao]:
        rows = self._fetchall(
            """
            SELECT id, produto_id, cor_id, tamanho_id, codigo_barras, codigo_interno
            FROM produto_variacao WHERE produto_id = %s
            ORDER BY id
            """,
            [produto_id],
        )
        return [ProdutoVariacao(*row) for row in rows]