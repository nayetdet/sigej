from typing import Optional
from dataclasses import dataclass

@dataclass
class EquipeManutencao:
    id: Optional[int] = None
    nome: Optional[str] = None
    turno: Optional[str] = None
