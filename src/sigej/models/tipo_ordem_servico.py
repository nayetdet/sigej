from dataclasses import dataclass

@dataclass
class TipoOrdemServico:
    id: int | None = None
    descricao: str | None = None
