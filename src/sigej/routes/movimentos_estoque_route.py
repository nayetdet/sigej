from decimal import Decimal, InvalidOperation
from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("movimentos_bp", __name__)

@bp.route("/movimentos-estoque", methods=["GET", "POST"])
def movimentos():
    if request.method == "POST":
        variacao_id = ParseUtils.to_int(request.form.get("produto_variacao_id", ""))
        local_id = ParseUtils.to_int(request.form.get("local_estoque_id", ""))
        tipo_movimento_id = ParseUtils.to_int(request.form.get("tipo_movimento_id", ""))
        funcionario_id = ParseUtils.to_int(request.form.get("funcionario_id", ""))
        os_id = ParseUtils.to_int(request.form.get("ordem_servico_id", ""))
        observacao = request.form.get("observacao", "").strip() or None
        try:
            quantidade = Decimal(request.form.get("quantidade", "0").strip())
        except (InvalidOperation, AttributeError):
            flash("Quantidade inválida.")
            return redirect(url_for("movimentos_bp.movimentos"))

        if not variacao_id or not local_id or not tipo_movimento_id:
            flash("Variação, local e tipo de movimento são obrigatórios.")
            return redirect(url_for("movimentos_bp.movimentos"))
        try:
            mov_id = ServiceInstance.get_estoque_service().registrar_movimento(
                produto_variacao_id=variacao_id,
                local_id=local_id,
                quantidade=quantidade,
                tipo_movimento_id=tipo_movimento_id,
                funcionario_id=funcionario_id,
                os_id=os_id,
                observacao=observacao,
            )

            flash(f"Movimento registrado com ID {mov_id}.")
        except Exception as exc:
            flash(f"Erro ao registrar movimento: {exc}")
        return redirect(url_for("movimentos_bp.movimentos"))

    return render_template(
        "cadastro_movimento_estoque.html",
        movimentos=ServiceInstance.get_estoque_service().listar_movimentos(),
        variacoes=ServiceInstance.get_produto_variacao_service().listar_todas(),
        locais=ServiceInstance.get_local_estoque_service().listar(),
        tipos_movimento=ServiceInstance.get_tipo_movimento_service().listar(),
        funcionarios=ServiceInstance.get_funcionario_service().listar(),
        ordens=ServiceInstance.get_ordem_servico_service().listar(),
    )
