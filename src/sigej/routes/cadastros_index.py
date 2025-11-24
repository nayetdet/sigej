from flask import Blueprint, render_template

bp = Blueprint("cadastros_index_bp", __name__)

@bp.route("/cadastros")
def cadastros():
    return render_template("cadastros_index.html")
