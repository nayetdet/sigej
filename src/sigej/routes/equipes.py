from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("equipes_bp", __name__)

@bp.route("/equipes", methods=["GET", "POST"])
def equipes():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        turno = request.form.get("turno", "").strip()
        if not nome or not turno:
            flash("Nome e turno são obrigatórios.")
            return redirect(url_for("equipes_bp.equipes"))
        try:
            equipe_id = ServiceInstance.get_equipe_service().criar(nome=nome, turno=turno)
            flash(f"Equipe cadastrada com ID {equipe_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar equipe: {exc}")
        return redirect(url_for("equipes_bp.equipes"))

    return render_template("cadastro_equipe.html", equipes=ServiceInstance.get_equipe_service().listar())
