from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.equipe_membro import EquipeMembro

class EquipeMembroDAO(BaseDAO):
    def insert(self, membro: EquipeMembro) -> int:
        sql = """
        INSERT INTO equipe_membro (equipe_id, funcionario_id, data_inicio, data_fim, funcao)
        VALUES (%s, %s, %s, %s, %s) RETURNING id
        """
        return self._execute_returning_id(
            sql, [membro.equipe_id, membro.funcionario_id, membro.data_inicio, membro.data_fim, membro.funcao]
        )

    def list_by_equipe(self, equipe_id: int) -> list[EquipeMembro]:
        rows = self._fetchall(
            """
            SELECT id, equipe_id, funcionario_id, data_inicio, data_fim, funcao
            FROM equipe_membro WHERE equipe_id = %s
            ORDER BY data_inicio DESC
            """,
            [equipe_id],
        )
        return [EquipeMembro(*row) for row in rows]
