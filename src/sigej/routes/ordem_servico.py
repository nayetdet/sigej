from datetime import date
from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("os_bp", __name__)

def _carregar_dados_os():
    return {
        "pessoas": ServiceInstance.get_pessoa_service().listar(),
        "areas": ServiceInstance.get_area_service().listar_areas(),
        "tipos_os": ServiceInstance.get_tipo_os_service().listar(),
        "equipes": ServiceInstance.get_equipe_service().listar(),
        "funcionarios": _listar_funcionarios_com_pessoa(),
        "tipos_funcionarios": ServiceInstance.get_tipo_funcionario_service().listar(),
        "setores": ServiceInstance.get_setor_service().listar(),
        "today": date.today(),
    }


def _listar_funcionarios_com_pessoa():
    funcionarios = []
    pessoa_service = ServiceInstance.get_pessoa_service()
    for func in ServiceInstance.get_funcionario_service().listar():
        pessoa = pessoa_service.buscar(func.pessoa_id)
        funcionarios.append(
            {
                "id": func.id,
                "pessoa_id": func.pessoa_id,
                "nome": pessoa.nome if pessoa else f"Funcionário {func.id}",
            }
        )
    return funcionarios

@bp.route("/os/nova", methods=["GET", "POST"])
def nova_os():
    if request.method == "POST":
        solicitante_id = ParseUtils.to_int(request.form.get("solicitante_id", ""))
        area_id = ParseUtils.to_int(request.form.get("area_id", ""))
        tipo_os_id = ParseUtils.to_int(request.form.get("tipo_os_id", ""))
        equipe_id = ParseUtils.to_int(request.form.get("equipe_id", ""))
        lider_id = ParseUtils.to_int(request.form.get("lider_id", ""))
        prioridade = ParseUtils.to_int(request.form.get("prioridade", ""))
        descricao = request.form.get("descricao", "").strip()

        try:
            os_id = ServiceInstance.get_ordem_servico_service().abrir_os(
                solicitante_id=solicitante_id,
                area_campus_id=area_id,
                tipo_os_id=tipo_os_id,
                equipe_id=equipe_id,
                lider_id=lider_id,
                prioridade=prioridade or 3,
                descricao_problema=descricao or "Sem descrição.",
            )
            flash(f"OS criada com ID {os_id}")
            return redirect(url_for("home_bp.home"))
        except Exception as exc:
            flash(f"Erro ao criar OS: {exc}")

    return render_template("os_form.html", **_carregar_dados_os())
