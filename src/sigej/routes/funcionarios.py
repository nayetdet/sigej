from datetime import date
from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("funcionarios_bp", __name__)

@bp.route("/funcionarios/novo", methods=["GET", "POST"])
def cadastro_funcionario():
    if request.method == "POST":
        pessoa_id = ParseUtils.to_int(request.form.get("pessoa_id", ""))
        tipo_func_id = ParseUtils.to_int(request.form.get("tipo_funcionario_id", ""))
        setor_id = ParseUtils.to_int(request.form.get("setor_id", ""))
        data_adm_str = request.form.get("data_admissao", "") or date.today().isoformat()
        if not pessoa_id or not tipo_func_id or not setor_id:
            flash("Pessoa, tipo e setor são obrigatórios.")
            return redirect(url_for("funcionarios_bp.cadastro_funcionario"))
        try:
            data_adm = date.fromisoformat(data_adm_str)
            func_id = ServiceInstance.get_funcionario_service().admitir(
                pessoa_id=pessoa_id,
                tipo_funcionario_id=tipo_func_id,
                setor_id=setor_id,
                data_admissao=data_adm,
            )
            flash(f"Funcionário cadastrado com ID {func_id}.")
        except Exception as exc:
            flash(f"Erro ao cadastrar funcionário: {exc}")
        return redirect(url_for("funcionarios_bp.cadastro_funcionario"))

    return render_template(
        "cadastro_funcionario.html",
        pessoas=ServiceInstance.get_pessoa_service().listar(),
        tipos_funcionarios=ServiceInstance.get_tipo_funcionario_service().listar(),
        setores=ServiceInstance.get_setor_service().listar(),
        funcionarios=ServiceInstance.get_funcionario_service().listar(),
        today=date.today(),
    )
