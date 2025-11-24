from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("unidades_bp", __name__)

@bp.route("/unidades-medida", methods=["GET", "POST"])
def unidades():
    if request.method == "POST":
        sigla = request.form.get("sigla", "").strip()
        descricao = request.form.get("descricao", "").strip() or None
        if not sigla:
            flash("Sigla é obrigatória.")
            return redirect(url_for("unidades_bp.unidades"))
        try:
            unidade_id = ServiceInstance.get_unidade_medida_service().criar(sigla=sigla, descricao=descricao)
            flash(f"Unidade cadastrada com ID {unidade_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar unidade: {exc}")
        return redirect(url_for("unidades_bp.unidades"))

    return render_template(
        "cadastro_unidade.html",
        unidades=ServiceInstance.get_unidade_medida_service().listar()
    )
