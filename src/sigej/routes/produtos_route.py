from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("produtos_bp", __name__)

@bp.route("/produtos", methods=["GET", "POST"])
def produtos():
    if request.method == "POST":
        descricao = request.form.get("descricao", "").strip()
        categoria_id = ParseUtils.to_int(request.form.get("categoria_id", ""))
        unidade_id = ParseUtils.to_int(request.form.get("unidade_medida_id", ""))
        marca_id = ParseUtils.to_int(request.form.get("marca_id", ""))
        if not descricao:
            flash("Descrição é obrigatória.")
            return redirect(url_for("produtos_bp.produtos"))
        try:
            produto_id = ServiceInstance.get_produto_service().criar(
                descricao=descricao,
                categoria_id=categoria_id,
                unidade_medida_id=unidade_id,
                marca_id=marca_id,
            )

            flash(f"Produto cadastrado com ID {produto_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar produto: {exc}")
        return redirect(url_for("produtos_bp.produtos"))

    return render_template(
        "cadastro_produto.html",
        produtos=ServiceInstance.get_produto_service().listar(),
        categorias=ServiceInstance.get_categoria_service().listar(),
        unidades=ServiceInstance.get_unidade_medida_service().listar(),
        marcas=ServiceInstance.get_marca_service().listar(),
    )
