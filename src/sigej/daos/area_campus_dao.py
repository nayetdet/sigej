from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.area_campus import AreaCampus

class AreaCampusDAO(BaseDAO):
    def insert(self, area: AreaCampus) -> int:
        sql = """
        INSERT INTO area_campus (tipo_area_id, descricao, bloco)
        VALUES (%s, %s, %s) RETURNING id
        """
        return self._execute_returning_id(sql, [area.tipo_area_id, area.descricao, area.bloco])

    def list_all(self) -> list[AreaCampus]:
        rows = self._fetchall("SELECT id, tipo_area_id, descricao, bloco FROM area_campus ORDER BY descricao")
        return [AreaCampus(*row) for row in rows]

    def find_by_id(self, area_id: Optional[int]) -> AreaCampus:
        row = self._fetchone("SELECT id, tipo_area_id, descricao, bloco FROM area_campus WHERE id = %s", [area_id])
        return AreaCampus(*row) if row else None