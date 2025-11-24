from flask import Flask
from src.sigej.config import Config
from src.sigej.routes.home import bp as home_bp
from src.sigej.routes.pessoas import bp as pessoas_bp
from src.sigej.routes.ordem_servico import bp as os_bp
from src.sigej.routes.solicitantes import bp as solicitantes_bp
from src.sigej.routes.areas import bp as areas_bp
from src.sigej.routes.tipos_area import bp as tipos_area_bp
from src.sigej.routes.tipos_os import bp as tipos_os_bp
from src.sigej.routes.equipes import bp as equipes_bp
from src.sigej.routes.funcionarios import bp as funcionarios_bp
from src.sigej.routes.setores import bp as setores_bp
from src.sigej.routes.tipos_funcionario import bp as tipos_funcionario_bp

def create_app() -> Flask:
    app = Flask(__name__)
    app.config["SECRET_KEY"] = Config.Flask.SECRET_KEY

    app.register_blueprint(home_bp)
    app.register_blueprint(pessoas_bp)
    app.register_blueprint(os_bp)
    app.register_blueprint(solicitantes_bp)
    app.register_blueprint(areas_bp)
    app.register_blueprint(tipos_area_bp)
    app.register_blueprint(tipos_os_bp)
    app.register_blueprint(setores_bp)
    app.register_blueprint(tipos_funcionario_bp)
    app.register_blueprint(equipes_bp)
    app.register_blueprint(funcionarios_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
