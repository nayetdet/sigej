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

    def list_all(self) -> list[OrdemServico]:
        rows = self._fetchall(
            """
            SELECT id, numero_sequencial, solicitante_id, area_campus_id, tipo_os_id,
                   equipe_id, lider_id, status_id, prioridade, data_abertura, data_prevista, descricao_problema
            FROM ordem_servico
            ORDER BY data_abertura DESC
            """
        )
        return [OrdemServico(*row) for row in rows]
