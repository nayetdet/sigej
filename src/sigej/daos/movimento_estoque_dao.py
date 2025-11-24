from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.movimento_estoque import MovimentoEstoque

class MovimentoEstoqueDAO(BaseDAO):
    def insert(self, movimento: MovimentoEstoque, conn=None) -> int:
        sql = """
        INSERT INTO movimento_estoque (
            produto_variacao_id, local_estoque_id, tipo_movimento_id, quantidade,
            data_hora, funcionario_id, ordem_servico_id, observacao
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """
        return self._execute_returning_id(
            sql,
            [
                movimento.produto_variacao_id,
                movimento.local_estoque_id,
                movimento.tipo_movimento_id,
                movimento.quantidade,
                movimento.data_hora,
                movimento.funcionario_id,
                movimento.ordem_servico_id,
                movimento.observacao,
            ],
            conn=conn,
        )

    def list_all(self) -> list[tuple]:
        return self._fetchall(
            """
            SELECT me.id, me.data_hora, tm.descricao, tm.sinal,
                   pv.codigo_interno, le.descricao AS local, me.quantidade,
                   me.funcionario_id, me.ordem_servico_id, me.observacao
            FROM movimento_estoque me
            JOIN tipo_movimento_estoque tm ON me.tipo_movimento_id = tm.id
            JOIN produto_variacao pv ON me.produto_variacao_id = pv.id
            JOIN local_estoque le ON me.local_estoque_id = le.id
            ORDER BY me.data_hora DESC
            """
        )
