from typing import Optional
from decimal import Decimal
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.estoque import Estoque

class EstoqueDAO(BaseDAO):
    def upsert(self, estoque: Estoque, conn=None):
        sql = """
        INSERT INTO estoque (produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (produto_variacao_id, local_estoque_id)
        DO UPDATE SET quantidade = EXCLUDED.quantidade, ponto_reposicao = EXCLUDED.ponto_reposicao
        """
        self._execute(
            sql,
            [estoque.produto_variacao_id, estoque.local_estoque_id, estoque.quantidade, estoque.ponto_reposicao],
            conn=conn,
        )

    def ajustar_quantidade(self, produto_variacao_id: int, local_id: int, delta: Decimal, conn=None):
        sql = """
        UPDATE estoque
        SET quantidade = quantidade + %s
        WHERE produto_variacao_id = %s AND local_estoque_id = %s
        """
        self._execute(sql, [delta, produto_variacao_id, local_id], conn=conn)

    def find(self, produto_variacao_id: int, local_id: Optional[int], conn=None) -> Estoque:
        row = self._fetchone(
            """
            SELECT produto_variacao_id, local_estoque_id, quantidade, ponto_reposicao
            FROM estoque
            WHERE produto_variacao_id = %s AND local_estoque_id = %s
            """,
            [produto_variacao_id, local_id],
            conn=conn,
        )
        return Estoque(*row) if row else None

    def abaixo_ponto_reposicao(self) -> list[tuple]:
        return self._fetchall(
            """
            SELECT p.descricao, pv.codigo_interno, le.descricao, e.quantidade, e.ponto_reposicao
            FROM estoque e
            JOIN produto_variacao pv ON e.produto_variacao_id = pv.id
            JOIN produto p ON pv.produto_id = p.id
            JOIN local_estoque le ON e.local_estoque_id = le.id
            WHERE e.quantidade < e.ponto_reposicao
            """
        )
