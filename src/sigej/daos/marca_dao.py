from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.marca import Marca

class MarcaDAO(BaseDAO):
    def insert(self, marca: Marca) -> int:
        return self._execute_returning_id(
            "INSERT INTO marca (nome) VALUES (%s) RETURNING id",
            [marca.nome],
        )

    def list_all(self) -> list[Marca]:
        rows = self._fetchall("SELECT id, nome FROM marca ORDER BY nome")
        return [Marca(*row) for row in rows]

    def find_by_id(self, marca_id: int) -> Marca:
        row = self._fetchone("SELECT id, nome FROM marca WHERE id = %s", [marca_id])
        return Marca(*row) if row else None
