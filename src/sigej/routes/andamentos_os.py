from datetime import datetime
from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("andamentos_os_bp", __name__)

@bp.route("/andamentos-os", methods=["GET", "POST"])
def andamentos_os():
    os_service = ServiceInstance.get_ordem_servico_service()
    if request.method == "POST":
        os_id = ParseUtils.to_int(request.form.get("os_id", ""))
        novo_status_id = ParseUtils.to_int(request.form.get("status_id", ""))
        funcionario_id = ParseUtils.to_int(request.form.get("funcionario_id", ""))
        descricao = request.form.get("descricao", "").strip() or "Atualização de status"
        if not os_id or not novo_status_id or not funcionario_id:
            flash("OS, status e funcionário são obrigatórios.")
            return redirect(url_for("andamentos_os_bp.andamentos_os", os_id=os_id or ""))
        try:
            os_service.atualizar_status(
                os_id=os_id,
                novo_status_id=novo_status_id,
                funcionario_id=funcionario_id,
                descricao=descricao,
                inicio_atendimento=datetime.now(),
            )
            flash("Andamento registrado.")
        except Exception as exc:
            flash(f"Erro ao registrar andamento: {exc}")
        return redirect(url_for("andamentos_os_bp.andamentos_os", os_id=os_id))

    os_id_param = ParseUtils.to_int(request.args.get("os_id", "") or "")
    timeline = os_service.timeline(os_id_param) if os_id_param else []
    return render_template(
        "cadastro_andamento_os.html",
        os_id=os_id_param,
        ordens=os_service.listar(),
        status_list=ServiceInstance.get_status_os_service().listar(),
        funcionarios=ServiceInstance.get_funcionario_service().listar(),
        timeline=timeline,
    )
