from typing import Optional
from src.sigej.daos.base_dao import BaseDAO
from src.sigej.models.pessoa import Pessoa

class PessoaDAO(BaseDAO):
    def insert(self, pessoa: Pessoa) -> int:
        sql = """
        INSERT INTO pessoa (nome, cpf, matricula_siape, email, telefone, ativo)
        VALUES (%s, %s, %s, %s, %s, %s)
        RETURNING id
        """
        return self._execute_returning_id(
            sql,
            [
                pessoa.nome,
                pessoa.cpf,
                pessoa.matricula_siape,
                pessoa.email,
                pessoa.telefone,
                pessoa.ativo,
            ],
        )

    def find_by_id(self, pessoa_id: Optional[int]) -> Pessoa:
        row = self._fetchone(
            "SELECT id, nome, cpf, matricula_siape, email, telefone, ativo FROM pessoa WHERE id = %s",
            [pessoa_id],
        )
        return Pessoa(*row) if row else None

    def list_all(self) -> list[Pessoa]:
        rows = self._fetchall(
            "SELECT id, nome, cpf, matricula_siape, email, telefone, ativo FROM pessoa ORDER BY id"
        )
        return [Pessoa(*row) for row in rows]

    def update(self, pessoa: Pessoa):
        sql = """
        UPDATE pessoa
        SET nome = %s, cpf = %s, matricula_siape = %s, email = %s, telefone = %s, ativo = %s
        WHERE id = %s
        """
        self._execute(
            sql,
            [
                pessoa.nome,
                pessoa.cpf,
                pessoa.matricula_siape,
                pessoa.email,
                pessoa.telefone,
                pessoa.ativo,
                pessoa.id,
            ],
        )

    def delete(self, pessoa_id: int):
        self._execute("DELETE FROM pessoa WHERE id = %s", [pessoa_id])