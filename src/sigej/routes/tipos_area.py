from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("tipos_area_bp", __name__)

@bp.route("/tipos-area", methods=["GET", "POST"])
def tipos_area():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("tipos_area_bp.tipos_area"))
        try:
            tipo_id = ServiceInstance.get_area_service().criar_tipo_area(descricao=descricao)
            flash(f"Tipo de área cadastrado com ID {tipo_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar tipo de área: {exc}")
        return redirect(url_for("tipos_area_bp.tipos_area"))

    return render_template(
        "cadastro_tipo_area.html",
        tipos_area=ServiceInstance.get_area_service().listar_tipos(),
    )
