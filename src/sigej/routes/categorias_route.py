from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("categorias_bp", __name__)

@bp.route("/categorias", methods=["GET", "POST"])
def categorias():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        if not nome:
            flash("Nome é obrigatório.")
            return redirect(url_for("categorias_bp.categorias"))
        try:
            categoria_id = ServiceInstance.get_categoria_service().criar(nome=nome)
            flash(f"Categoria cadastrada com ID {categoria_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar categoria: {exc}")
        return redirect(url_for("categorias_bp.categorias"))

    return render_template(
        "cadastro_categoria.html",
        categorias=ServiceInstance.get_categoria_service().listar(),
    )
