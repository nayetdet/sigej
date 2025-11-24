from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.ordem_servico import OrdemServico

class OrdemServicoDAO(BaseDAO):
    def insert(self, os: OrdemServico, conn=None) -> int:
        sql = """
        INSERT INTO ordem_servico (
            numero_sequencial, solicitante_id, area_campus_id, tipo_os_id, equipe_id,
            lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        RETURNING id
        """
        return self._execute_returning_id(
            sql,
            [
                os.numero_sequencial,
                os.solicitante_id,
                os.area_campus_id,
                os.tipo_os_id,
                os.equipe_id,
                os.lider_id,
                os.status_id,
                os.prioridade,
                os.data_abertura,
                os.data_prevista,
                os.descricao_problema,
            ],
            conn=conn,
        )

    def find_by_id(self, os_id: Optional[int]) -> OrdemServico:
        row = self._fetchone(
            """
            SELECT id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id,
                   equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema
            FROM ordem_servico
            WHERE id = %s
            """,
            [os_id],
        )
        return OrdemServico(*row) if row else None

    def update_status(self, os_id: int, novo_status_id: int, conn=None):
        self._execute("UPDATE ordem_servico SET status_id = %s WHERE id = %s", [novo_status_id, os_id], conn=conn)

    def em_aberto_por_prioridade_area(self) -> list[tuple]:
        return self._fetchall(
            """
            SELECT os.id, os.numero_sequencial, os.prioridade, ac.descricao AS area, tos.descricao AS tipo_servico,
                   p.nome AS solicitante, os.data_abertura
            FROM ordem_servico os
            JOIN area_campus ac ON os.area_campus_id = ac.id
            JOIN tipo_ordem_servico tos ON os.tipo_os_id = tos.id
            JOIN status_ordem_servico sts ON os.status_id = sts.id
            JOIN pessoa p ON os.solicitante_id = p.id
            WHERE sts.descricao IN ('aberta', 'em_atendimento', 'aguardando_material')
            ORDER BY os.prioridade ASC, os.data_abertura ASC
            """
        )