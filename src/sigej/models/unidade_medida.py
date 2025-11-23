from dataclasses import dataclass

@dataclass
class UnidadeMedida:
    id: int | None = None
    sigla: str | None = None
    descricao: str | None = None
