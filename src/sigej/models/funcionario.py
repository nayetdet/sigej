from dataclasses import dataclass
from datetime import date

@dataclass
class Funcionario:
    id: int | None = None
    pessoa_id: int | None = None
    tipo_funcionario_id: int | None = None
    setor_id: int | None = None
    data_admissao: date | None = None
    data_demissao: date | None = None
