from dataclasses import dataclass

@dataclass
class LocalEstoque:
    id: int | None = None
    descricao: str | None = None
    responsavel_id: int | None = None
