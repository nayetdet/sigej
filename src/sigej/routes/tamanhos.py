from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("tamanhos_bp", __name__)

@bp.route("/tamanhos", methods=["GET", "POST"])
def tamanhos():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("tamanhos_bp.tamanhos"))
        try:
            tamanho_id = ServiceInstance.get_tamanho_service().criar(descricao=descricao)
            flash(f"Tamanho cadastrado com ID {tamanho_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar tamanho: {exc}")
        return redirect(url_for("tamanhos_bp.tamanhos"))

    return render_template("cadastro_tamanho.html", tamanhos=ServiceInstance.get_tamanho_service().listar())
