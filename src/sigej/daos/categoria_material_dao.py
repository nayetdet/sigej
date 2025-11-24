from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.categoria_material import CategoriaMaterial

class CategoriaMaterialDAO(BaseDAO):
    def insert(self, categoria: CategoriaMaterial) -> int:
        return self._execute_returning_id(
            "INSERT INTO categoria_material (nome) VALUES (%s) RETURNING id", [categoria.nome]
        )

    def list_all(self) -> list[CategoriaMaterial]:
        rows = self._fetchall("SELECT id, nome FROM categoria_material ORDER BY nome")
        return [CategoriaMaterial(*row) for row in rows]

    def find_by_id(self, categoria_id: int) -> CategoriaMaterial:
        row = self._fetchone("SELECT id, nome FROM categoria_material WHERE id = %s", [categoria_id])
        return CategoriaMaterial(*row) if row else None
