from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.andamento_ordem_servico import AndamentoOrdemServico

class AndamentoOrdemServicoDAO(BaseDAO):
    def insert(self, andamento: AndamentoOrdemServico, conn=None) -> int:
        sql = """
        INSERT INTO andamento_ordem_servico (
            os_id, data_hora, status_anterior_id, status_novo_id, funcionario_id, descricao,
            inicio_atendimento, fim_atendimento
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """

        return self._execute_returning_id(
            sql,
            [
                andamento.os_id,
                andamento.data_hora,
                andamento.status_anterior_id,
                andamento.status_novo_id,
                andamento.funcionario_id,
                andamento.descricao,
                andamento.inicio_atendimento,
                andamento.fim_atendimento,
            ],
            conn=conn,
        )

    def timeline(self, os_id: int) -> list[tuple]:
        return self._fetchall(
            """
            SELECT a.data_hora, pes.nome AS funcionario, sts_novo.descricao AS status_atual, a.descricao
            FROM andamento_ordem_servico a
            JOIN funcionario f ON a.funcionario_id = f.id
            JOIN pessoa pes ON f.pessoa_id = pes.id
            JOIN status_ordem_servico sts_novo ON a.status_novo_id = sts_novo.id
            WHERE a.os_id = %s
            ORDER BY a.data_hora
            """,
            [os_id],
        )
