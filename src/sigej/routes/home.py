from flask import Blueprint, render_template
from src.sigej.deps.service_instance import ServiceInstance
bp = Blueprint("home_bp", __name__)

@bp.route("/")
def home():
    os_abertas = ServiceInstance.get_relatorios_service().os_em_aberto_por_prioridade_area()
    materiais_baixos = ServiceInstance.get_relatorios_service().materiais_abaixo_ponto_reposicao()
    return render_template("index.html", os_abertas=os_abertas, materiais_baixos=materiais_baixos)
