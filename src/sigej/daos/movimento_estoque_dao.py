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
