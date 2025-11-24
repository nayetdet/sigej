from typing import Optional
from dataclasses import dataclass
from datetime import date

@dataclass
class Funcionario:
    id: Optional[int] = None
    pessoa_id: Optional[int] = None
    tipo_funcionario_id: Optional[int] = None
    setor_id: Optional[int] = None
    data_admissao: Optional[date] = None
    data_demissao: Optional[date] = None
