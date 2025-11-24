import logging
import random
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional
from faker import Faker
from src.sigej.database import database
from src.sigej.deps.dao_instance import DAOInstance
from src.sigej.deps.service_instance import ServiceInstance
from src.sigej.models.estoque import Estoque

class DatabaseSeeder:
    __fake = Faker("pt_BR")

    @classmethod
    def truncate_tables(cls) -> None:
        tables = [
            "andamento_ordem_servico",
            "item_ordem_servico",
            "ordem_servico",
            "movimento_estoque",
            "estoque",
            "local_estoque",
            "produto_variacao",
            "tamanho",
            "cor",
            "produto",
            "marca",
            "unidade_medida",
            "categoria_material",
            "fornecedor",
            "equipe_membro",
            "equipe_manutencao",
            "funcionario",
            "pessoa",
            "tipo_funcionario",
            "setor",
            "area_campus",
            "tipo_area_campus",
            "tipo_movimento_estoque",
            "tipo_ordem_servico",
            "status_ordem_servico",
        ]

        with database.connection() as conn:
            with conn.cursor() as cur:
                cur.execute(f"TRUNCATE {', '.join(tables)} RESTART IDENTITY CASCADE;")
            conn.commit()

    @classmethod
    def seed_tipos_funcionario(cls) -> list[int]:
        descricoes = ["tecnico", "analista", "coordenador", "terceirizado"]
        return [ServiceInstance.get_tipo_funcionario_service().criar(desc) for desc in descricoes]

    @classmethod
    def seed_setores(cls) -> list[int]:
        nomes = ["Administrativo", "Infraestrutura", "Operacoes", "TI", "Financeiro"]
        setores = []
        for nome in nomes:
            sigla = "".join(word[0] for word in nome.split())[:10]
            setores.append(ServiceInstance.get_setor_service().criar(nome=nome, sigla=sigla))
        return setores

    @classmethod
    def seed_pessoas(cls, total: int = 40) -> list[int]:
        pessoas_ids = []
        for _ in range(total):
            cpf = str(cls.__fake.unique.random_number(digits=11, fix_len=True)).zfill(11)
            pessoas_ids.append(
                ServiceInstance.get_pessoa_service().cadastrar(
                    nome=cls.__fake.name(),
                    cpf=cpf,
                    matricula=f"S{cls.__fake.random_int(10000, 99999)}",
                    email=cls.__fake.unique.email(),
                    telefone=cls.__fake.msisdn()[:20],
                )
            )
        return pessoas_ids

    @classmethod
    def seed_funcionarios(
        cls,
        pessoas_ids: list[int],
        tipos_ids: list[int],
        setores_ids: list[int],
        total: int = 15
    ) -> list[int]:
        escolhidos = random.sample(pessoas_ids, total)
        funcionarios_ids = []
        for pessoa_id in escolhidos:
            admissao = cls.__fake.date_between(start_date="-2y", end_date="-30d")
            funcionarios_ids.append(
                ServiceInstance.get_funcionario_service().admitir(
                    pessoa_id=pessoa_id,
                    tipo_funcionario_id=random.choice(tipos_ids),
                    setor_id=random.choice(setores_ids),
                    data_admissao=admissao,
                )
            )
        return funcionarios_ids

    @classmethod
    def seed_tipos_area(cls) -> list[int]:
        descricoes = ["Administrativa", "Academica", "Externa"]
        return [ServiceInstance.get_area_service().criar_tipo_area(desc) for desc in descricoes]

    @classmethod
    def seed_areas(cls, tipo_ids: list[int], total: int = 8) -> list[int]:
        blocos = ["A", "B", "C", "D", "E"]
        areas_ids = []
        for _ in range(total):
            areas_ids.append(
                ServiceInstance.get_area_service().criar_area(
                    descricao=cls.__fake.street_name(),
                    bloco=random.choice(blocos),
                    tipo_area_id=random.choice(tipo_ids),
                )
            )
        return areas_ids

    @classmethod
    def seed_equipes(cls, total: int = 5) -> list[int]:
        nomes = ["Equipe Alfa", "Equipe Bravo", "Equipe Delta", "Equipe Eco", "Equipe Fox"]
        turnos = ["manha", "tarde", "noite"]
        equipes_ids = []
        for nome in random.sample(nomes, total):
            equipes_ids.append(ServiceInstance.get_equipe_service().criar(nome=nome, turno=random.choice(turnos)))
        return equipes_ids

    @classmethod
    def seed_equipe_membros(cls, equipes_ids: list[int], funcionarios_ids: list[int]) -> list[int]:
        membros_ids = []
        for equipe_id in equipes_ids:
            quantidade = random.randint(3, min(5, len(funcionarios_ids)))
            for funcionario_id in random.sample(funcionarios_ids, quantidade):
                inicio = cls.__fake.date_between(start_date="-1y", end_date="-10d")
                fim = None if random.random() < 0.8 else cls.__fake.date_between(start_date=inicio, end_date="today")
                membros_ids.append(
                    ServiceInstance.get_equipe_membro_service().adicionar_membro(
                        equipe_id=equipe_id,
                        funcionario_id=funcionario_id,
                        data_inicio=inicio,
                        data_fim=fim,
                        funcao=random.choice(["tecnico", "apoio", "coordenador"]),
                    )
                )
        return membros_ids

    @classmethod
    def seed_categorias(cls) -> list[int]:
        nomes = ["Materiais Gerais", "Elétrica", "Hidraulica", "TI", "Ferramentas"]
        return [ServiceInstance.get_categoria_service().criar(nome) for nome in nomes]

    @classmethod
    def seed_unidades(cls) -> list[int]:
        unidades = [
            ("UN", "Unidade"),
            ("KG", "Kilograma"),
            ("M", "Metro"),
            ("L", "Litro"),
        ]
        return [ServiceInstance.get_unidade_medida_service().criar(sigla=sigla, descricao=desc) for sigla, desc in unidades]

    @classmethod
    def seed_fornecedores(cls, total: int = 8) -> list[int]:
        fornecedores_ids = []
        for _ in range(total):
            fornecedores_ids.append(
                ServiceInstance.get_fornecedor_service().criar(
                    nome=cls.__fake.company(),
                    cnpj=cls.__fake.cnpj()
                )
            )
        return fornecedores_ids

    @classmethod
    def seed_marcas(cls, total: int = 8) -> list[int]:
        marcas_ids = []
        for _ in range(total):
            marcas_ids.append(ServiceInstance.get_marca_service().criar(nome=cls.__fake.unique.company_suffix()))
        return marcas_ids

    @classmethod
    def seed_cores(cls) -> list[int]:
        nomes = ["vermelho", "azul", "preto", "branco", "cinza", "verde"]
        return [ServiceInstance.get_cor_service().criar(nome) for nome in nomes]

    @classmethod
    def seed_tamanhos(cls) -> list[int]:
        descricoes = ["PP", "P", "M", "G", "GG", "U"]
        return [ServiceInstance.get_tamanho_service().criar(descricao) for descricao in descricoes]

    @classmethod
    def seed_produtos(
        cls,
        categorias_ids: list[int],
        unidades_ids: list[int],
        marcas_ids: list[int],
        total: int = 12
    ) -> list[int]:
        produtos_ids = []
        for _ in range(total):
            produtos_ids.append(
                ServiceInstance.get_produto_service().criar(
                    descricao=cls.__fake.catch_phrase(),
                    categoria_id=random.choice(categorias_ids),
                    unidade_medida_id=random.choice(unidades_ids),
                    marca_id=random.choice(marcas_ids),
                )
            )
        return produtos_ids

    @classmethod
    def seed_variacoes(cls, produtos_ids: list[int], cores_ids: list[int], tamanhos_ids: list[int]) -> list[int]:
        variacoes_ids = []
        combinacoes_usadas: set[tuple[int, int, int]] = set()
        for produto_id in produtos_ids:
            cores_escolhidas = random.sample(cores_ids, random.randint(2, min(4, len(cores_ids))))
            tamanhos_escolhidos = random.sample(tamanhos_ids, random.randint(2, min(4, len(tamanhos_ids))))
            for cor_id in cores_escolhidas:
                tamanho_id = random.choice(tamanhos_escolhidos)
                if (produto_id, cor_id, tamanho_id) in combinacoes_usadas:
                    continue

                combinacoes_usadas.add((produto_id, cor_id, tamanho_id))
                variacoes_ids.append(
                    ServiceInstance.get_produto_variacao_service().criar(
                        produto_id=produto_id,
                        cor_id=cor_id,
                        tamanho_id=tamanho_id,
                        codigo_barras=cls.__fake.unique.ean(length=13),
                        codigo_interno=f"PRD-{cls.__fake.random_int(1000, 9999)}",
                    )
                )
        return variacoes_ids

    @classmethod
    def seed_locais(cls, funcionarios_ids: list[int], total: int = 5) -> list[int]:
        locais_ids = []
        for idx in range(total):
            descricao = f"Deposito {idx + 1}"
            responsavel_id = random.choice(funcionarios_ids)
            locais_ids.append(
                ServiceInstance.get_local_estoque_service().criar(descricao=descricao, responsavel_id=responsavel_id)
            )
        return locais_ids

    @classmethod
    def seed_tipos_movimento(cls) -> dict[str, int]:
        tipos = [
            ("Entrada", "+"),
            ("Saida", "-"),
            ("Ajuste", "+"),
        ]

        ids = {}
        for descricao, sinal in tipos:
            tipo_id = ServiceInstance.get_tipo_movimento_service().criar(descricao=descricao, sinal=sinal)
            ids[descricao.lower()] = tipo_id
        return ids

    @classmethod
    def seed_estoque(
        cls,
        variacoes_ids: list[int],
        locais_ids: list[int],
        tipo_movimentos: dict[str, int],
        funcionarios_ids: list[int],
        os_ids: Optional[list[int]] = None,
    ) -> list[tuple[int, int]]:
        estoque_pairs = []
        for variacao_id in variacoes_ids:
            local_id = random.choice(locais_ids)
            ponto_reposicao = Decimal(random.randint(5, 10))
            DAOInstance.get_estoque_dao().upsert(
                Estoque(
                    produto_variacao_id=variacao_id,
                    local_estoque_id=local_id,
                    quantidade=Decimal("0"),
                    ponto_reposicao=ponto_reposicao,
                )
            )

            quantidade = Decimal(f"{random.uniform(5, 40):.2f}")
            mov_id = ServiceInstance.get_estoque_service().registrar_movimento(
                produto_variacao_id=variacao_id,
                local_id=local_id,
                quantidade=quantidade,
                tipo_movimento_id=tipo_movimentos["entrada"],
                funcionario_id=random.choice(funcionarios_ids),
                os_id=random.choice(os_ids) if os_ids else None,
                observacao="Carga inicial",
            )

            if os_ids:
                alvo = datetime(2025, 10, random.randint(1, 30), random.randint(7, 18), random.randint(0, 59))
                DAOInstance.get_movimento_estoque_dao()._execute(
                    "UPDATE movimento_estoque SET data_hora = %s, ordem_servico_id = %s WHERE id = %s",
                    [alvo, random.choice(os_ids), mov_id],
                )

            estoque_pairs.append((variacao_id, local_id))
        return estoque_pairs

    @classmethod
    def seed_movimentos_extras(
        cls,
        estoque_pairs: list[tuple[int, int]],
        tipo_movimentos: dict[str, int],
        funcionarios_ids: list[int],
        os_ids: Optional[list[int]] = None,
    ) -> None:
        for variacao_id, local_id in random.sample(estoque_pairs, k=max(1, len(estoque_pairs) // 3)):
            quantidade = Decimal(f"{random.uniform(1, 5):.2f}")
            tipo_id = random.choice([tipo_movimentos["saida"], tipo_movimentos["ajuste"]])
            mov_id = ServiceInstance.get_estoque_service().registrar_movimento(
                produto_variacao_id=variacao_id,
                local_id=local_id,
                quantidade=quantidade,
                tipo_movimento_id=tipo_id,
                funcionario_id=random.choice(funcionarios_ids),
                os_id=random.choice(os_ids) if os_ids else None,
                observacao="Movimento automatizado",
            )

            if os_ids:
                alvo = datetime(2025, 10, random.randint(1, 30), random.randint(7, 18), random.randint(0, 59))
                DAOInstance.get_movimento_estoque_dao()._execute(
                    "UPDATE movimento_estoque SET data_hora = %s, ordem_servico_id = %s WHERE id = %s",
                    [alvo, random.choice(os_ids), mov_id],
                )

    @classmethod
    def seed_tipos_os(cls) -> list[int]:
        descricoes = ["Manutencao eletrica", "Manutencao hidraulica", "Infraestrutura", "TI"]
        return [ServiceInstance.get_tipo_os_service().criar(desc) for desc in descricoes]

    @classmethod
    def seed_status_os(cls) -> list[int]:
        descricoes = ["aberta", "em_atendimento", "aguardando_material", "concluída", "cancelada"]
        return [ServiceInstance.get_status_os_service().criar(desc) for desc in descricoes]

    @classmethod
    def seed_ordens_servico(
        cls,
        solicitantes_ids: list[int],
        areas_ids: list[int],
        tipos_os_ids: list[int],
        equipes_ids: list[int],
        lideres_ids: list[int],
        variacoes_ids: list[int],
        total: int = 6,
    ) -> list[int]:
        os_ids = []
        base_data = datetime(2025, 10, 10)
        for idx in range(total):
            abertura = base_data + timedelta(days=random.randint(-20, 20))
            previsao = abertura.date() + timedelta(days=random.randint(2, 10))
            itens = []
            for variacao_id in random.sample(variacoes_ids, random.randint(1, 3)):
                itens.append(
                    {
                        "produto_variacao_id": variacao_id,
                        "quantidade_prevista": Decimal(f"{random.uniform(1, 4):.1f}"),
                        "quantidade_usada": None,
                    }
                )

            os_id = ServiceInstance.get_ordem_servico_service().abrir_os(
                solicitante_id=random.choice(solicitantes_ids),
                area_campus_id=random.choice(areas_ids),
                tipo_os_id=random.choice(tipos_os_ids),
                equipe_id=random.choice(equipes_ids),
                lider_id=random.choice(lideres_ids),
                prioridade=random.randint(1, 5),
                descricao_problema=cls.__fake.sentence(nb_words=12),
                data_prevista=datetime.combine(previsao, datetime.min.time()),
                numero_sequencial=f"OS-{idx + 1:04d}",
                itens=itens,
            )

            os_ids.append(os_id)
        return os_ids

    @classmethod
    def seed_andamentos(cls, ordens_ids: list[int], status_ids: list[int], lideres_ids: list[int]) -> None:
        for os_id in ordens_ids:
            if random.random() > 0.2:
                ServiceInstance.get_ordem_servico_service().atualizar_status(
                    os_id=os_id,
                    novo_status_id=random.choice(status_ids),
                    funcionario_id=random.choice(lideres_ids),
                    descricao="Atualizacao automatica",
                    inicio_atendimento=datetime.now() - timedelta(days=random.randint(0, 3)),
                    fim_atendimento=None,
                )

    @classmethod
    def run(cls) -> None:
        cls.truncate_tables()
        tipos_func = cls.seed_tipos_funcionario()
        setores = cls.seed_setores()
        pessoas = cls.seed_pessoas()
        funcionarios = cls.seed_funcionarios(pessoas, tipos_func, setores)

        tipos_area = cls.seed_tipos_area()
        areas = cls.seed_areas(tipos_area)
        equipes = cls.seed_equipes()
        cls.seed_equipe_membros(equipes, funcionarios)

        categorias = cls.seed_categorias()
        unidades = cls.seed_unidades()
        cls.seed_fornecedores()
        marcas = cls.seed_marcas()
        cores = cls.seed_cores()
        tamanhos = cls.seed_tamanhos()
        produtos = cls.seed_produtos(categorias, unidades, marcas)
        variacoes = cls.seed_variacoes(produtos, cores, tamanhos)

        tipos_os = cls.seed_tipos_os()
        status_os = cls.seed_status_os()
        ordens = cls.seed_ordens_servico(
            solicitantes_ids=pessoas,
            areas_ids=areas,
            tipos_os_ids=tipos_os,
            equipes_ids=equipes,
            lideres_ids=funcionarios,
            variacoes_ids=variacoes,
        )

        tipo_movimentos = cls.seed_tipos_movimento()
        locais = cls.seed_locais(funcionarios)
        estoque_pairs = cls.seed_estoque(variacoes, locais, tipo_movimentos, funcionarios, os_ids=ordens)
        cls.seed_movimentos_extras(estoque_pairs, tipo_movimentos, funcionarios, os_ids=ordens)
        cls.seed_andamentos(ordens, status_os, funcionarios)
        logging.info("Base de dados populada com sucesso.")

def main():
    DatabaseSeeder.run()

if __name__ == "__main__":
    main()
