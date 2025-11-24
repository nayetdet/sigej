from src.sigej.daos.base_dao import BaseDAO

class RelatoriosDAO(BaseDAO):
    def os_em_aberto_por_prioridade_area(self) -> list[tuple]:
        return self._fetchall(
            """
            SELECT os.id, os.numero_sequencial, os.prioridade, ac.descricao AS area, tos.descricao AS tipo_servico,
                   p.nome AS solicitante, os.data_abertura
            FROM ordem_servico os
            JOIN area_campus ac ON os.area_campus_id = ac.id
            JOIN tipo_ordem_servico tos ON os.tipo_os_id = tos.id
            JOIN status_ordem_servico sts ON os.status_id = sts.id
            JOIN pessoa p ON os.solicitante_id = p.id
            WHERE replace(lower(sts.descricao), ' ', '_') IN ('aberta', 'em_atendimento', 'aguardando_material')
            ORDER BY os.prioridade ASC, os.data_abertura ASC
            """
        )

    def materiais_abaixo_ponto_reposicao(self) -> list[tuple]:
        return self._fetchall(
            """
            SELECT p.descricao, pv.codigo_interno, le.descricao AS local, e.quantidade, e.ponto_reposicao
            FROM estoque e
            JOIN produto_variacao pv ON e.produto_variacao_id = pv.id
            JOIN produto p ON pv.produto_id = p.id
            JOIN local_estoque le ON e.local_estoque_id = le.id
            WHERE e.quantidade < e.ponto_reposicao
            """
        )

    def consumo_por_equipe_periodo(self, inicio: str, fim: str) -> list[tuple]:
        return self._fetchall(
            """
            SELECT eq.nome AS equipe, p.descricao, SUM(me.quantidade) AS total
            FROM movimento_estoque me
            JOIN produto_variacao pv ON me.produto_variacao_id = pv.id
            JOIN produto p ON pv.produto_id = p.id
            JOIN ordem_servico os ON me.ordem_servico_id = os.id
            JOIN equipe_manutencao eq ON os.equipe_id = eq.id
            WHERE me.data_hora BETWEEN %s AND %s
            GROUP BY eq.nome, p.descricao
            """,
            [inicio, fim],
        )

    def os_concluidas_por_tipo_no_ano(self, ano: int) -> list[tuple]:
        return self._fetchall(
            """
            SELECT tos.descricao, COUNT(*) AS total
            FROM ordem_servico os
            JOIN tipo_ordem_servico tos ON os.tipo_os_id = tos.id
            JOIN status_ordem_servico sts ON os.status_id = sts.id
            WHERE replace(lower(sts.descricao), 'í', 'i') = 'concluida' AND EXTRACT(YEAR FROM os.data_abertura) = %s
            GROUP BY tos.descricao
            """,
            [ano],
        )
