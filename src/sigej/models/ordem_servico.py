from typing import Optional
from dataclasses import dataclass
from datetime import date, datetime

@dataclass
class OrdemServico:
    id: Optional[int] = None
    numero_sequencial: Optional[str] = None
    solicitante_id: Optional[int] = None
    area_campus_id: Optional[int] = None
    tipo_os_id: Optional[int] = None
    equipe_id: Optional[int] = None
    lider_id: Optional[int] = None
    status_id: int = 1
    prioridade: Optional[int] = None
    data_abertura: Optional[datetime] = None
    data_prevista: Optional[date] = None
    descricao_problema: Optional[str] = None
