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
from src.sigej.routes.cadastros_index import bp as cadastros_index_bp
from src.sigej.routes.categorias import bp as categorias_bp
from src.sigej.routes.unidades_medida import bp as unidades_bp
from src.sigej.routes.marcas import bp as marcas_bp
from src.sigej.routes.fornecedores import bp as fornecedores_bp
from src.sigej.routes.cores import bp as cores_bp
from src.sigej.routes.tamanhos import bp as tamanhos_bp
from src.sigej.routes.produtos import bp as produtos_bp
from src.sigej.routes.produto_variacoes import bp as variacoes_bp
from src.sigej.routes.locais_estoque import bp as locais_estoque_bp
from src.sigej.routes.tipos_movimento import bp as tipos_movimento_bp
from src.sigej.routes.status_os import bp as status_os_bp
from src.sigej.routes.equipe_membros import bp as equipe_membros_bp
from src.sigej.routes.itens_os import bp as itens_os_bp
from src.sigej.routes.andamentos_os import bp as andamentos_os_bp
from src.sigej.routes.movimentos_estoque import bp as movimentos_bp

def create_app() -> Flask:
    app = Flask(
        __name__,
        template_folder=str(Config.Paths.ROOT / "resources" / "templates"),
        static_folder=str(Config.Paths.ROOT / "resources" / "static"),
        static_url_path="/static",
    )
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
    app.register_blueprint(cadastros_index_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(unidades_bp)
    app.register_blueprint(marcas_bp)
    app.register_blueprint(fornecedores_bp)
    app.register_blueprint(cores_bp)
    app.register_blueprint(tamanhos_bp)
    app.register_blueprint(produtos_bp)
    app.register_blueprint(variacoes_bp)
    app.register_blueprint(locais_estoque_bp)
    app.register_blueprint(tipos_movimento_bp)
    app.register_blueprint(status_os_bp)
    app.register_blueprint(equipe_membros_bp)
    app.register_blueprint(itens_os_bp)
    app.register_blueprint(andamentos_os_bp)
    app.register_blueprint(movimentos_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
