from dataclasses import dataclass

@dataclass
class TipoFuncionario:
    id: int | None = None
    descricao: str | None = None
