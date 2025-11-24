from typing import Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class EquipeMembro:
    id: Optional[int] = None
    equipe_id: Optional[int] = None
    funcionario_id: Optional[int] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    funcao: Optional[str] = None
