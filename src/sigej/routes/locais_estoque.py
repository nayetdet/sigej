from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("locais_estoque_bp", __name__)

@bp.route("/locais-estoque", methods=["GET", "POST"])
def locais_estoque():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        responsavel_id = ParseUtils.to_int(request.form.get("responsavel_id", ""))
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("locais_estoque_bp.locais_estoque"))
        try:
            local_id = ServiceInstance.get_local_estoque_service().criar(
                descricao=descricao,
                responsavel_id=responsavel_id
            )

            flash(f"Local cadastrado com ID {local_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar local: {exc}")
        return redirect(url_for("locais_estoque_bp.locais_estoque"))

    return render_template(
        "cadastro_local_estoque.html",
        locais=ServiceInstance.get_local_estoque_service().listar(),
        funcionarios=ServiceInstance.get_funcionario_service().listar(),
    )
