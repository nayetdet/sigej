from typing import Optional, List
from src.sigej.daos.area_campus_dao import AreaCampusDAO
from src.sigej.daos.tipo_area_campus_dao import TipoAreaCampusDAO
from src.sigej.models.area_campus import AreaCampus
from src.sigej.models.tipo_area_campus import TipoAreaCampus

class AreaService:
    def __init__(self, area_dao: AreaCampusDAO, tipo_area_dao: TipoAreaCampusDAO):
        self.__area_dao = area_dao
        self.__tipo_area_dao = tipo_area_dao

    def listar_areas(self) -> List[AreaCampus]:
        return self.__area_dao.list_all()

    def listar_tipos(self) -> List[TipoAreaCampus]:
        return self.__tipo_area_dao.list_all()

    def criar_area(self, descricao: str, bloco: Optional[str] = None, tipo_area_id: Optional[int] = None) -> int:
        area = AreaCampus(descricao=descricao, bloco=bloco, tipo_area_id=tipo_area_id)
        return self.__area_dao.insert(area)

    def criar_tipo_area(self, descricao: str) -> int:
        tipo = TipoAreaCampus(descricao=descricao)
        return self.__tipo_area_dao.insert(tipo)
