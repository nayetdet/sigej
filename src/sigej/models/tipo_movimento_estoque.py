from dataclasses import dataclass

@dataclass
class TipoMovimentoEstoque:
    id: int | None = None
    descricao: str | None = None
    sinal: str | None = None
