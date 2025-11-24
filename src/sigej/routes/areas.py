from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("areas_bp", __name__)

@bp.route("/areas", methods=["GET", "POST"])
def areas():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        bloco = request.form.get("bloco", "").strip() or None
        tipo_area_id = ParseUtils.to_int(request.form.get("tipo_area_id", ""))
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("areas_bp.areas"))
        try:
            area_id = ServiceInstance.get_area_service().criar_area(
                descricao=descricao,
                bloco=bloco,
                tipo_area_id=tipo_area_id
            )

            flash(f"Área cadastrada com ID {area_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar área: {exc}")
        return redirect(url_for("areas_bp.areas"))

    return render_template(
        "cadastro_area.html",
        areas=ServiceInstance.get_area_service().listar_areas(),
        tipos_area=ServiceInstance.get_area_service().listar_tipos(),
    )
