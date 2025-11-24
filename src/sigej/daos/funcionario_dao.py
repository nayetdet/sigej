from typing import Optional
from datetime import date
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.funcionario import Funcionario

class FuncionarioDAO(BaseDAO):
    def insert(self, funcionario: Funcionario) -> int:
        sql = """
        INSERT INTO funcionario (pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id
        """
        return self._execute_returning_id(
            sql,
            [
                funcionario.pessoa_id,
                funcionario.tipo_funcionario_id,
                funcionario.setor_id,
                funcionario.data_admissao,
                funcionario.data_demissao,
            ],
        )

    def find_by_id(self, funcionario_id: Optional[int]) -> Funcionario:
        row = self._fetchone(
            """
            SELECT id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao
            FROM funcionario WHERE id = %s
            """,
            [funcionario_id],
        )
        return Funcionario(*row) if row else None

    def list_all(self) -> list[Funcionario]:
        rows = self._fetchall(
            """
            SELECT id, pessoa_id, tipo_funcionario_id, setor_id, data_admissao, data_demissao
            FROM funcionario ORDER BY id
            """
        )
        return [Funcionario(*row) for row in rows]

    def demitir(self, funcionario_id: int, data_demissao: date):
        self._execute("UPDATE funcionario SET data_demissao = %s WHERE id = %s", [data_demissao, funcionario_id])
