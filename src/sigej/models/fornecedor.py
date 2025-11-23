from dataclasses import dataclass

@dataclass
class Fornecedor:
    id: int | None = None
    nome: str | None = None
    cnpj: str | None = None
