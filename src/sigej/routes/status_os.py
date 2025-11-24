from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("status_os_bp", __name__)

@bp.route("/status-os", methods=["GET", "POST"])
def status_os():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("status_os_bp.status_os"))
        try:
            status_id = ServiceInstance.get_status_os_service().criar(descricao=descricao)
            flash(f"Status cadastrado com ID {status_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar status: {exc}")
        return redirect(url_for("status_os_bp.status_os"))

    return render_template("cadastro_status_os.html", status_list=ServiceInstance.get_status_os_service().listar())
