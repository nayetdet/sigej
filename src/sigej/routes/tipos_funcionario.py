from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("tipos_funcionario_bp", __name__)

@bp.route("/tipos-funcionario", methods=["GET", "POST"])
def tipos_funcionario():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("tipos_funcionario_bp.tipos_funcionario"))
        try:
            tipo_id = ServiceInstance.get_tipo_funcionario_service().criar(descricao=descricao)
            flash(f"Tipo de funcionário cadastrado com ID {tipo_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar tipo de funcionário: {exc}")
        return redirect(url_for("tipos_funcionario_bp.tipos_funcionario"))

    return render_template(
        "cadastro_tipo_funcionario.html",
        tipos=ServiceInstance.get_tipo_funcionario_service().listar(),
    )
