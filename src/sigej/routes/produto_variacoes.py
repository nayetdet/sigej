from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("variacoes_bp", __name__)

@bp.route("/produtos/variacoes", methods=["GET", "POST"])
def variacoes():
    produto_service = ServiceInstance.get_produto_service()
    variacao_service = ServiceInstance.get_produto_variacao_service()

    if request.method == "POST":
        produto_id = ParseUtils.to_int(request.form.get("produto_id", ""))
        cor_id = ParseUtils.to_int(request.form.get("cor_id", ""))
        tamanho_id = ParseUtils.to_int(request.form.get("tamanho_id", ""))
        codigo_barras = request.form.get("codigo_barras", "").strip() or None
        codigo_interno = request.form.get("codigo_interno", "").strip() or None
        if not produto_id:
            flash("Produto é obrigatório.")
            return redirect(url_for("variacoes_bp.variacoes"))
        try:
            variacao_id = variacao_service.criar(
                produto_id=produto_id,
                cor_id=cor_id,
                tamanho_id=tamanho_id,
                codigo_barras=codigo_barras,
                codigo_interno=codigo_interno,
            )
            flash(f"Variação cadastrada com ID {variacao_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar variação: {exc}")
        return redirect(url_for("variacoes_bp.variacoes"))

    produtos = produto_service.listar()
    variacoes_por_produto = {p.id: variacao_service.listar_por_produto(p.id) for p in produtos}
    return render_template(
        "cadastro_produto_variacao.html",
        produtos=produtos,
        cores=ServiceInstance.get_cor_service().listar(),
        tamanhos=ServiceInstance.get_tamanho_service().listar(),
        variacoes_por_produto=variacoes_por_produto,
    )
