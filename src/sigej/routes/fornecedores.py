from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance

bp = Blueprint("fornecedores_bp", __name__)

@bp.route("/fornecedores", methods=["GET", "POST"])
def fornecedores():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        cnpj = request.form.get("cnpj", "").strip() or None
        if not nome:
            flash("Nome é obrigatório.")
            return redirect(url_for("fornecedores_bp.fornecedores"))
        try:
            fornecedor_id = ServiceInstance.get_fornecedor_service().criar(nome=nome, cnpj=cnpj)
            flash(f"Fornecedor cadastrado com ID {fornecedor_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar fornecedor: {exc}")
        return redirect(url_for("fornecedores_bp.fornecedores"))

    return render_template("cadastro_fornecedor.html", fornecedores=ServiceInstance.get_fornecedor_service().listar())
