from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("tipos_os_bp", __name__)

@bp.route("/tipos-os", methods=["GET", "POST"])
def tipos_os():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("tipos_os_bp.tipos_os"))
        try:
            tipo_id = ServiceInstance.get_tipo_os_service().criar(descricao=descricao)
            flash(f"Tipo de OS cadastrado com ID {tipo_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar tipo de OS: {exc}")
        return redirect(url_for("tipos_os_bp.tipos_os"))

    return render_template(
        "cadastro_tipo_os.html",
        tipos=ServiceInstance.get_tipo_os_service().listar(),
    )
