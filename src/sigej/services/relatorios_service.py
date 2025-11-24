from src.sigej.daos.relatorios_dao import RelatoriosDAO

class RelatoriosService:
    def __init__(self, relatorios_dao: RelatoriosDAO):
        self.__relatorios_dao = relatorios_dao

    def os_em_aberto_por_prioridade_area(self):
        return self.__relatorios_dao.os_em_aberto_por_prioridade_area()

    def materiais_abaixo_ponto_reposicao(self):
        return self.__relatorios_dao.materiais_abaixo_ponto_reposicao()

    def consumo_por_equipe_periodo(self, inicio: str, fim: str):
        return self.__relatorios_dao.consumo_por_equipe_periodo(inicio, fim)

    def os_concluidas_por_tipo_no_ano(self, ano: int):
        return self.__relatorios_dao.os_concluidas_por_tipo_no_ano(ano)
