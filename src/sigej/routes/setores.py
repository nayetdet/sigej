from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("setores_bp", __name__)

@bp.route("/setores", methods=["GET", "POST"])
def setores():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        sigla = request.form.get("sigla", "").strip() or None
        if not nome:
            flash("Nome é obrigatório.")
            return redirect(url_for("setores_bp.setores"))
        try:
            setor_id = ServiceInstance.get_setor_service().criar(nome=nome, sigla=sigla)
            flash(f"Setor cadastrado com ID {setor_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar setor: {exc}")
        return redirect(url_for("setores_bp.setores"))

    return render_template("cadastro_setor.html", setores=ServiceInstance.get_setor_service().listar())
