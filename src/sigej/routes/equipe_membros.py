from datetime import date
from flask import Blueprint, flash, redirect, render_template, request, url_for
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.utils.parse_utils import ParseUtils

bp = Blueprint("equipe_membros_bp", __name__)

@bp.route("/equipes/membros", methods=["GET", "POST"])
def equipe_membros():
    equipe_service = ServiceInstance.get_equipe_service()
    membros_service = ServiceInstance.get_equipe_membro_service()

    if request.method == "POST":
        equipe_id = ParseUtils.to_int(request.form.get("equipe_id", ""))
        funcionario_id = ParseUtils.to_int(request.form.get("funcionario_id", ""))
        data_inicio_str = request.form.get("data_inicio", "") or date.today().isoformat()
        funcao = request.form.get("funcao", "").strip() or None
        data_fim_str = request.form.get("data_fim", "").strip() or None

        if not equipe_id or not funcionario_id:
            flash("Equipe e funcionário são obrigatórios.")
            return redirect(url_for("equipe_membros_bp.equipe_membros"))
        try:
            data_inicio = date.fromisoformat(data_inicio_str)
            data_fim = date.fromisoformat(data_fim_str) if data_fim_str else None
            membro_id = membros_service.adicionar_membro(
                equipe_id=equipe_id,
                funcionario_id=funcionario_id,
                data_inicio=data_inicio,
                funcao=funcao,
                data_fim=data_fim,
            )

            flash(f"Membro adicionado com ID {membro_id}.")
        except Exception as exc:
            flash(f"Erro ao adicionar membro: {exc}")
        return redirect(url_for("equipe_membros_bp.equipe_membros"))

    equipes = equipe_service.listar()
    funcionarios = ServiceInstance.get_funcionario_service().listar()
    membros_por_equipe = {e.id: membros_service.listar_por_equipe(e.id) for e in equipes}
    return render_template(
        "cadastro_equipe_membro.html",
        equipes=equipes,
        funcionarios=funcionarios,
        membros_por_equipe=membros_por_equipe,
        today=date.today(),
    )
