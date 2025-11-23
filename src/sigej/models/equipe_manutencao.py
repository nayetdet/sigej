from dataclasses import dataclass

@dataclass
class EquipeManutencao:
    id: int | None = None
    nome: str | None = None
    turno: str | None = None
