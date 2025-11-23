from dataclasses import dataclass
from datetime import date

@dataclass
class EquipeMembro:
    id: int | None = None
    equipe_id: int | None = None
    funcionario_id: int | None = None
    data_inicio: date | None = None
    data_fim: date | None = None
    funcao: str | None = None
