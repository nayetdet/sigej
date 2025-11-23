from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class OrdemServico:
    id: int | None = None
    numero_sequencial: str | None = None
    solicitante_id: int | None = None
    area_campus_id: int | None = None
    tipo_os_id: int | None = None
    equipe_id: int | None = None
    lider_id: int | None = None
    status_id: int = 1
    prioridade: int | None = None
    data_abertura: datetime | None = None
    data_prevista: date | None = None
    descricao_problema: str | None = None
