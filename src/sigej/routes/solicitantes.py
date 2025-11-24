from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("solicitantes_bp", __name__)

@bp.route("/solicitantes", methods=["GET", "POST"])
def solicitantes():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        cpf = request.form.get("cpf", "").strip() or None
        email = request.form.get("email", "").strip() or None
        telefone = request.form.get("telefone", "").strip() or None
        if not nome:
            flash("Nome é obrigatório.")
            return redirect(url_for("solicitantes_bp.solicitantes"))
        try:
            pessoa_id = ServiceInstance.get_pessoa_service().cadastrar(
                nome=nome, cpf=cpf, email=email, telefone=telefone
            )
            flash(f"Solicitante cadastrado com ID {pessoa_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar solicitante: {exc}")
        return redirect(url_for("solicitantes_bp.solicitantes"))

    return render_template(
        "cadastro_solicitante.html",
        pessoas=ServiceInstance.get_pessoa_service().listar(),
    )
