from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("pessoas_bp", __name__)

@bp.route("/pessoas", methods=["GET", "POST"])
def pessoas():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        cpf = request.form.get("cpf", "").strip() or None
        email = request.form.get("email", "").strip() or None
        telefone = request.form.get("telefone", "").strip() or None

        if not nome:
            flash("Nome é obrigatório.")
        else:
            try:
                ServiceInstance.get_pessoa_service().cadastrar(nome=nome, cpf=cpf, email=email, telefone=telefone)
                flash("Pessoa cadastrada com sucesso.")
                return redirect(url_for("pessoas_bp.pessoas"))
            except Exception as exc:
                flash(f"Erro ao cadastrar: {exc}")

    pessoas_lista = ServiceInstance.get_pessoa_service().listar()
    return render_template("pessoas.html", pessoas=pessoas_lista)
