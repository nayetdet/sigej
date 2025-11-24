from typing import Optional
from dataclasses import dataclass
from datetime import datetime

@dataclass
class AndamentoOrdemServico:
    id: Optional[int] = None
    os_id: Optional[int] = None
    data_hora: Optional[datetime] = None
    status_anterior_id: Optional[int] = None
    status_novo_id: Optional[int] = None
    funcionario_id: Optional[int] = None
    descricao: Optional[str] = None
    inicio_atendimento: Optional[datetime] = None
    fim_atendimento: Optional[datetime] = None
