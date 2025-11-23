from dataclasses import dataclass

@dataclass
class StatusOrdemServico:
    id: int | None = None
    descricao: str | None = None
