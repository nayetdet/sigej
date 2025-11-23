from dataclasses import dataclass

@dataclass
class Pessoa:
    id: int | None = None
    nome: str | None = None
    cpf: str | None = None
    matricula_siape: str | None = None
    email: str | None = None
    telefone: str | None = None
    ativo: bool = True
