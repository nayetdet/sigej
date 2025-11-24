from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("itens_os_bp", __name__)

@bp.route("/itens-os", methods=["GET", "POST"])
def itens_os():
    os_id_param = ParseUtils.to_int(request.args.get("os_id", "") or "")
    item_service = ServiceInstance.get_ordem_servico_service()
    ordens = item_service.listar()

    if request.method == "POST":
        os_id = ParseUtils.to_int(request.form.get("os_id", ""))
        variacao_id = ParseUtils.to_int(request.form.get("produto_variacao_id", ""))
        qtd_prevista_str = request.form.get("quantidade_prevista", "").strip()
        qtd_usada_str = request.form.get("quantidade_usada", "").strip()
        qtd_prevista = float(qtd_prevista_str) if qtd_prevista_str else None
        qtd_usada = float(qtd_usada_str) if qtd_usada_str else None

        if not os_id or not variacao_id:
            flash("OS e variação são obrigatórias.")
            return redirect(url_for("itens_os_bp.itens_os", os_id=os_id or ""))
        try:
            item_id = item_service.adicionar_item(
                os_id=os_id,
                produto_variacao_id=variacao_id,
                quantidade_prevista=qtd_prevista,
                quantidade_usada=qtd_usada,
            )

            flash(f"Item adicionado com ID {item_id}.")
        except Exception as exc:
            flash(f"Erro ao adicionar item: {exc}")
        return redirect(url_for("itens_os_bp.itens_os", os_id=os_id))

    os_selecionada = os_id_param or (ordens[0].id if ordens else None)
    itens = item_service.listar_itens(os_selecionada) if os_selecionada else []
    variacoes = ServiceInstance.get_produto_variacao_service().listar_todas()
    variacoes_dict = {v.id: v for v in variacoes}
    produtos = {p.id: p for p in ServiceInstance.get_produto_service().listar()}
    return render_template(
        "cadastro_item_os.html",
        os_id=os_selecionada,
        itens=itens,
        ordens=ordens,
        variacoes=variacoes,
        variacoes_dict=variacoes_dict,
        produtos=produtos,
    )
