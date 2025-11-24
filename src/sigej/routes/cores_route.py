from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("cores_bp", __name__)

@bp.route("/cores", methods=["GET", "POST"])
def cores():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        if not nome:
            flash("Nome é obrigatório.")
            return redirect(url_for("cores_bp.cores"))
        try:
            cor_id = ServiceInstance.get_cor_service().criar(nome=nome)
            flash(f"Cor cadastrada com ID {cor_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar cor: {exc}")
        return redirect(url_for("cores_bp.cores"))

    return render_template(
        "cadastro_cor.html",
        cores=ServiceInstance.get_cor_service().listar(),
    )
