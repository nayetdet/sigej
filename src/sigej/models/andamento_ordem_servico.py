from dataclasses import dataclass
from datetime import datetime

@dataclass
class AndamentoOrdemServico:
    id: int | None = None
    os_id: int | None = None
    data_hora: datetime | None = None
    status_anterior_id: int | None = None
    status_novo_id: int | None = None
    funcionario_id: int | None = None
    descricao: str | None = None
    inicio_atendimento: datetime | None = None
    fim_atendimento: datetime | None = None
