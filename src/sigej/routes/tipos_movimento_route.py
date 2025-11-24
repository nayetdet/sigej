from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("tipos_movimento_bp", __name__)

@bp.route("/tipos-movimento", methods=["GET", "POST"])
def tipos_movimento():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        sinal = request.form.get("sinal", "").strip()
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("tipos_movimento_bp.tipos_movimento"))
        try:
            tipo_id = ServiceInstance.get_tipo_movimento_service().criar(descricao=descricao, sinal=sinal)
            flash(f"Tipo de movimento cadastrado com ID {tipo_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar tipo de movimento: {exc}")
        return redirect(url_for("tipos_movimento_bp.tipos_movimento"))

    return render_template(
        "cadastro_tipo_movimento.html",
        tipos=ServiceInstance.get_tipo_movimento_service().listar(),
    )
