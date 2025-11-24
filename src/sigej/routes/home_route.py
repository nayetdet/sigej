from flask import Blueprint, render_template
from src.sigej.deps.service_instance import ServiceInstance
bp = Blueprint("home_bp", __name__)

@bp.route("/")
def home():
    os_abertas = ServiceInstance.get_relatorios_service().os_em_aberto_por_prioridade_area()
    materiais_baixos = ServiceInstance.get_relatorios_service().materiais_abaixo_ponto_reposicao()
    consumo_outubro = ServiceInstance.get_relatorios_service().consumo_por_equipe_periodo("2025-10-01", "2025-10-31")
    os_concluidas_ano = ServiceInstance.get_relatorios_service().os_concluidas_por_tipo_no_ano(2025)

    timeline_os = []
    os_id_timeline = os_abertas[0][0] if os_abertas else None
    if os_id_timeline:
        timeline_os = ServiceInstance.get_ordem_servico_service().timeline(os_id_timeline)

    return render_template(
        "index.html",
        os_abertas=os_abertas,
        materiais_baixos=materiais_baixos,
        consumo_outubro=consumo_outubro,
        os_concluidas_ano=os_concluidas_ano,
        os_id_timeline=os_id_timeline,
        timeline_os=timeline_os,
        sidebar_links=None,
    )
