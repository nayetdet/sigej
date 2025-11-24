from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.tipo_area_campus import TipoAreaCampus

class TipoAreaCampusDAO(BaseDAO):
    def insert(self, tipo: TipoAreaCampus) -> int:
        return self._execute_returning_id(
            "INSERT INTO tipo_area_campus (descricao) VALUES (%s) RETURNING id", [tipo.descricao]
        )

    def list_all(self) -> list[TipoAreaCampus]:
        rows = self._fetchall("SELECT id, descricao FROM tipo_area_campus ORDER BY descricao")
        return [TipoAreaCampus(*row) for row in rows]

    def find_by_id(self, tipo_id: Optional[int]) -> TipoAreaCampus:
        row = self._fetchone("SELECT id, descricao FROM tipo_area_campus WHERE id = %s", [tipo_id])
        return TipoAreaCampus(*row) if row else None
