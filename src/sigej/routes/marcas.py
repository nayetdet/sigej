from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("marcas_bp", __name__)

@bp.route("/marcas", methods=["GET", "POST"])
def marcas():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        if not nome:
            flash("Nome é obrigatório.")
            return redirect(url_for("marcas_bp.marcas"))
        try:
            marca_id = ServiceInstance.get_marca_service().criar(nome=nome)
            flash(f"Marca cadastrada com ID {marca_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar marca: {exc}")
        return redirect(url_for("marcas_bp.marcas"))

    return render_template("cadastro_marca.html", marcas=ServiceInstance.get_marca_service().listar())
