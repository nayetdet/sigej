from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.item_ordem_servico import ItemOrdemServico

class ItemOrdemServicoDAO(BaseDAO):
    def insert(self, item: ItemOrdemServico, conn=None) -> int:
        sql = """
        INSERT INTO item_ordem_servico (os_id, produto_variacao_id, quantidade_prevista, quantidade_usada)
        VALUES (%s, %s, %s, %s) RETURNING id
        """
        return self._execute_returning_id(
            sql, [item.os_id, item.produto_variacao_id, item.quantidade_prevista, item.quantidade_usada], conn=conn
        )

    def list_by_os(self, os_id: int) -> list[ItemOrdemServico]:
        rows = self._fetchall(
            """
            SELECT id, os_id, produto_variacao_id, quantidade_prevista, quantidade_usada
            FROM item_ordem_servico
            WHERE os_id = %s
            """,
            [os_id],
        )
        return [ItemOrdemServico(*row) for row in rows]
