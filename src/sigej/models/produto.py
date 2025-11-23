from dataclasses import dataclass

@dataclass
class Produto:
    id: int | None = None
    descricao: str | None = None
    categoria_id: int | None = None
    unidade_medida_id: int | None = None
    marca_id: int | None = None
