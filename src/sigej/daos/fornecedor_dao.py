from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.fornecedor import Fornecedor

class FornecedorDAO(BaseDAO):
    def insert(self, fornecedor: Fornecedor) -> int:
        return self._execute_returning_id(
            "INSERT INTO fornecedor (nome, cnpj) VALUES (%s, %s) RETURNING id",
            [fornecedor.nome, fornecedor.cnpj],
        )

    def list_all(self) -> list[Fornecedor]:
        rows = self._fetchall("SELECT id, nome, cnpj FROM fornecedor ORDER BY nome")
        return [Fornecedor(*row) for row in rows]
