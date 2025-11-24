from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.unidade_medida import UnidadeMedida

class UnidadeMedidaDAO(BaseDAO):
    def insert(self, unidade: UnidadeMedida) -> int:
        return self._execute_returning_id(
            "INSERT INTO unidade_medida (sigla, descricao) VALUES (%s, %s) RETURNING id",
            [unidade.sigla, unidade.descricao],
        )

    def list_all(self) -> list[UnidadeMedida]:
        rows = self._fetchall("SELECT id, sigla, descricao FROM unidade_medida ORDER BY sigla")
        return [UnidadeMedida(*row) for row in rows]

    def find_by_id(self, unidade_id: int) -> UnidadeMedida:
        row = self._fetchone("SELECT id, sigla, descricao FROM unidade_medida WHERE id = %s", [unidade_id])
        return UnidadeMedida(*row) if row else None
