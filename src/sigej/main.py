from flask import Flask
from src.sigej.config import Config
from src.sigej.routes.home_route import bp as home_bp
from src.sigej.routes.pessoas_route import bp as pessoas_bp
from src.sigej.routes.ordem_servico_route import bp as os_bp
from src.sigej.routes.solicitantes_route import bp as solicitantes_bp
from src.sigej.routes.areas_route import bp as areas_bp
from src.sigej.routes.tipos_area_route import bp as tipos_area_bp
from src.sigej.routes.tipos_os_route import bp as tipos_os_bp
from src.sigej.routes.equipes_route import bp as equipes_bp
from src.sigej.routes.funcionarios_route import bp as funcionarios_bp
from src.sigej.routes.setores_route import bp as setores_bp
from src.sigej.routes.tipos_funcionario_route import bp as tipos_funcionario_bp
from src.sigej.routes.cadastros_index_route import bp as cadastros_index_bp
from src.sigej.routes.categorias_route import bp as categorias_bp
from src.sigej.routes.unidades_medida_route import bp as unidades_bp
from src.sigej.routes.marcas_route import bp as marcas_bp
from src.sigej.routes.fornecedores_route import bp as fornecedores_bp
from src.sigej.routes.cores_route import bp as cores_bp
from src.sigej.routes.tamanhos_route import bp as tamanhos_bp
from src.sigej.routes.produtos_route import bp as produtos_bp
from src.sigej.routes.produto_variacoes_route import bp as variacoes_bp
from src.sigej.routes.locais_estoque_route import bp as locais_estoque_bp
from src.sigej.routes.tipos_movimento_route import bp as tipos_movimento_bp
from src.sigej.routes.status_os_route import bp as status_os_bp
from src.sigej.routes.equipe_membros_route import bp as equipe_membros_bp
from src.sigej.routes.itens_os_route import bp as itens_os_bp
from src.sigej.routes.andamentos_os_route import bp as andamentos_os_bp
from src.sigej.routes.movimentos_estoque_route import bp as movimentos_bp

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
