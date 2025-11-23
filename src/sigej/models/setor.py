from dataclasses import dataclass

@dataclass
class Setor:
    id: int | None = None
    nome: str | None = None
    sigla: str | None = None
