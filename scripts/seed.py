import logging
import random
from datetime import datetime, timedelta
from decimal import Decimal
from typing import Optional
from faker import Faker
from src.sigej.database import database
from src.sigej.deps.dao_instance import DAOInstance
from src.sigej.models.andamento_ordem_servico import AndamentoOrdemServico
from src.sigej.models.area_campus import AreaCampus
from src.sigej.models.categoria_material import CategoriaMaterial
from src.sigej.models.cor import Cor
from src.sigej.models.equipe_manutencao import EquipeManutencao
from src.sigej.models.equipe_membro import EquipeMembro
from src.sigej.models.estoque import Estoque
from src.sigej.models.fornecedor import Fornecedor
from src.sigej.models.funcionario import Funcionario
from src.sigej.models.item_ordem_servico import ItemOrdemServico
from src.sigej.models.local_estoque import LocalEstoque
from src.sigej.models.marca import Marca
from src.sigej.models.movimento_estoque import MovimentoEstoque
from src.sigej.models.ordem_servico import OrdemServico
from src.sigej.models.pessoa import Pessoa
from src.sigej.models.produto import Produto
from src.sigej.models.produto_variacao import ProdutoVariacao
from src.sigej.models.setor import Setor
from src.sigej.models.status_ordem_servico import StatusOrdemServico
from src.sigej.models.tamanho import Tamanho
from src.sigej.models.tipo_area_campus import TipoAreaCampus
from src.sigej.models.tipo_funcionario import TipoFuncionario
from src.sigej.models.tipo_movimento_estoque import TipoMovimentoEstoque
from src.sigej.models.tipo_ordem_servico import TipoOrdemServico
from src.sigej.models.unidade_medida import UnidadeMedida

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
        tipo_dao = DAOInstance.get_tipo_funcionario_dao()
        return [tipo_dao.insert(TipoFuncionario(descricao=desc)) for desc in descricoes]

    @classmethod
    def seed_setores(cls) -> list[int]:
        nomes = ["Administrativo", "Infraestrutura", "Operacoes", "TI", "Financeiro"]
        setores = []
        setor_dao = DAOInstance.get_setor_dao()
        for nome in nomes:
            setores.append(setor_dao.insert(Setor(nome=nome, sigla="".join(word[0] for word in nome.split())[:10])))
        return setores

    @classmethod
    def seed_pessoas(cls, total: int = 12) -> list[int]:
        pessoas_ids = []
        pessoa_dao = DAOInstance.get_pessoa_dao()
        for _ in range(total):
            pessoas_ids.append(
                pessoa_dao.insert(
                    Pessoa(
                        nome=cls.__fake.name(),
                        cpf=str(cls.__fake.unique.random_number(digits=11, fix_len=True)).zfill(11),
                        matricula_siape=f"S{cls.__fake.random_int(10000, 99999)}",
                        email=cls.__fake.unique.email(),
                        telefone=cls.__fake.msisdn()[:20],
                    )
                )
            )
        return pessoas_ids

    @classmethod
    def seed_funcionarios(
        cls,
        pessoas_ids: list[int],
        tipos_ids: list[int],
        setores_ids: list[int],
        total: int = 8
    ) -> list[int]:
        escolhidos = random.sample(pessoas_ids, total)
        funcionarios_ids = []
        funcionario_dao = DAOInstance.get_funcionario_dao()
        for pessoa_id in escolhidos:
            funcionarios_ids.append(
                funcionario_dao.insert(
                    Funcionario(
                        pessoa_id=pessoa_id,
                        tipo_funcionario_id=random.choice(tipos_ids),
                        setor_id=random.choice(setores_ids),
                        data_admissao=cls.__fake.date_between(start_date="-2y", end_date="-30d"),
                    )
                )
            )
        return funcionarios_ids

    @classmethod
    def seed_tipos_area(cls) -> list[int]:
        descricoes = ["Administrativa", "Academica", "Externa"]
        tipo_area_dao = DAOInstance.get_tipo_area_campus_dao()
        return [tipo_area_dao.insert(TipoAreaCampus(descricao=desc)) for desc in descricoes]

    @classmethod
    def seed_areas(cls, tipo_ids: list[int], total: int = 5) -> list[int]:
        blocos = ["A", "B", "C", "D", "E"]
        areas_ids = []
        area_dao = DAOInstance.get_area_campus_dao()
        for _ in range(total):
            areas_ids.append(
                area_dao.insert(
                    AreaCampus(
                        descricao=cls.__fake.street_name(),
                        bloco=random.choice(blocos),
                        tipo_area_id=random.choice(tipo_ids),
                    )
                )
            )
        return areas_ids

    @classmethod
    def seed_equipes(cls, total: int = 5) -> list[int]:
        nomes = ["Equipe Alfa", "Equipe Bravo", "Equipe Delta", "Equipe Eco", "Equipe Fox"]
        turnos = ["manha", "tarde", "noite"]
        equipes_ids = []
        equipe_dao = DAOInstance.get_equipe_manutencao_dao()
        for nome in random.sample(nomes, total):
            equipes_ids.append(equipe_dao.insert(EquipeManutencao(nome=nome, turno=random.choice(turnos))))
        return equipes_ids

    @classmethod
    def seed_equipe_membros(cls, equipes_ids: list[int], funcionarios_ids: list[int]) -> list[int]:
        membros_ids = []
        membro_dao = DAOInstance.get_equipe_membro_dao()
        for equipe_id in equipes_ids:
            quantidade = random.randint(3, min(5, len(funcionarios_ids)))
            for funcionario_id in random.sample(funcionarios_ids, quantidade):
                inicio = cls.__fake.date_between(start_date="-1y", end_date="-10d")
                membros_ids.append(
                    membro_dao.insert(
                        EquipeMembro(
                            equipe_id=equipe_id,
                            funcionario_id=funcionario_id,
                            data_inicio=inicio,
                            data_fim=None if random.random() < 0.8 else cls.__fake.date_between(start_date=inicio, end_date="today"),
                            funcao=random.choice(["tecnico", "apoio", "coordenador"]),
                        )
                    )
                )
        return membros_ids

    @classmethod
    def seed_categorias(cls) -> list[int]:
        nomes = ["Materiais Gerais", "Elétrica", "Hidraulica", "TI", "Ferramentas"]
        categoria_dao = DAOInstance.get_categoria_material_dao()
        return [categoria_dao.insert(CategoriaMaterial(nome=nome)) for nome in nomes]

    @classmethod
    def seed_unidades(cls) -> list[int]:
        unidades = [
            ("UN", "Unidade"),
            ("KG", "Kilograma"),
            ("M", "Metro"),
            ("L", "Litro"),
        ]
        unidade_dao = DAOInstance.get_unidade_medida_dao()
        return [unidade_dao.insert(UnidadeMedida(sigla=sigla, descricao=desc)) for sigla, desc in unidades]

    @classmethod
    def seed_fornecedores(cls, total: int = 5) -> list[int]:
        fornecedores_ids = []
        fornecedor_dao = DAOInstance.get_fornecedor_dao()
        for _ in range(total):
            fornecedores_ids.append(
                fornecedor_dao.insert(Fornecedor(nome=cls.__fake.company(), cnpj=cls.__fake.cnpj()))
            )
        return fornecedores_ids

    @classmethod
    def seed_marcas(cls, total: int = 5) -> list[int]:
        marcas_ids = []
        marca_dao = DAOInstance.get_marca_dao()
        for _ in range(total):
            marcas_ids.append(marca_dao.insert(Marca(nome=cls.__fake.unique.company_suffix())))
        return marcas_ids

    @classmethod
    def seed_cores(cls) -> list[int]:
        nomes = ["vermelho", "azul", "preto", "branco", "cinza", "verde"]
        cor_dao = DAOInstance.get_cor_dao()
        return [cor_dao.insert(Cor(nome=nome)) for nome in nomes]

    @classmethod
    def seed_tamanhos(cls) -> list[int]:
        descricoes = ["PP", "P", "M", "G", "GG", "U"]
        tamanho_dao = DAOInstance.get_tamanho_dao()
        return [tamanho_dao.insert(Tamanho(descricao=descricao)) for descricao in descricoes]

    @classmethod
    def seed_produtos(
        cls,
        categorias_ids: list[int],
        unidades_ids: list[int],
        marcas_ids: list[int],
        total: int = 6
    ) -> list[int]:
        produtos_ids = []
        produto_dao = DAOInstance.get_produto_dao()
        for _ in range(total):
            produtos_ids.append(
                produto_dao.insert(
                    Produto(
                        descricao=cls.__fake.catch_phrase(),
                        categoria_id=random.choice(categorias_ids),
                        unidade_medida_id=random.choice(unidades_ids),
                        marca_id=random.choice(marcas_ids),
                    )
                )
            )
        return produtos_ids

    @classmethod
    def seed_variacoes(cls, produtos_ids: list[int], cores_ids: list[int], tamanhos_ids: list[int]) -> list[int]:
        variacoes_ids = []
        combinacoes_usadas: set[tuple[int, int, int]] = set()
        variacao_dao = DAOInstance.get_produto_variacao_dao()
        for produto_id in produtos_ids:
            cores_escolhidas = random.sample(cores_ids, min(2, len(cores_ids)))
            tamanhos_escolhidos = random.sample(tamanhos_ids, min(2, len(tamanhos_ids)))
            for cor_id in cores_escolhidas:
                tamanho_id = random.choice(tamanhos_escolhidos)
                if (produto_id, cor_id, tamanho_id) in combinacoes_usadas:
                    continue

                combinacoes_usadas.add((produto_id, cor_id, tamanho_id))
                variacoes_ids.append(
                    variacao_dao.insert(
                        ProdutoVariacao(
                            produto_id=produto_id,
                            cor_id=cor_id,
                            tamanho_id=tamanho_id,
                            codigo_barras=cls.__fake.unique.ean(length=13),
                            codigo_interno=f"PRD-{cls.__fake.random_int(1000, 9999)}",
                        )
                    )
                )
        return variacoes_ids

    @classmethod
    def seed_locais(cls, funcionarios_ids: list[int], total: int = 5) -> list[int]:
        locais_ids = []
        local_dao = DAOInstance.get_local_estoque_dao()
        for idx in range(total):
            locais_ids.append(
                local_dao.insert(
                    LocalEstoque(
                        descricao=f"Deposito {idx + 1}",
                        responsavel_id=random.choice(funcionarios_ids),
                    )
                )
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
        tipo_movimento_dao = DAOInstance.get_tipo_movimento_estoque_dao()
        for descricao, sinal in tipos:
            ids[descricao.lower()] = tipo_movimento_dao.insert(TipoMovimentoEstoque(descricao=descricao, sinal=sinal))
        return ids

    @classmethod
    def registrar_movimento(
        cls,
        produto_variacao_id: int,
        local_id: int,
        quantidade: Decimal,
        tipo_movimento_id: int,
        funcionario_id: Optional[int] = None,
        os_id: Optional[int] = None,
        observacao: Optional[str] = None,
    ) -> int:
        tipo_movimento = DAOInstance.get_tipo_movimento_estoque_dao().find_by_id(tipo_movimento_id)
        if not tipo_movimento:
            raise ValueError("Tipo de movimento inválido")

        estoque_dao = DAOInstance.get_estoque_dao()
        movimento_dao = DAOInstance.get_movimento_estoque_dao()
        estoque_atual = estoque_dao.find(produto_variacao_id, local_id)

        if not estoque_atual:
            estoque_atual = Estoque(
                produto_variacao_id=produto_variacao_id,
                local_estoque_id=local_id,
                quantidade=Decimal("0"),
                ponto_reposicao=Decimal("5"),
            )
            estoque_dao.upsert(estoque_atual)

        if tipo_movimento.sinal == "-" and estoque_atual.quantidade < quantidade:
            quantidade = estoque_atual.quantidade

        delta = quantidade if tipo_movimento.sinal == "+" else -quantidade
        novo_movimento_id = movimento_dao.insert(
            MovimentoEstoque(
                produto_variacao_id=produto_variacao_id,
                local_estoque_id=local_id,
                tipo_movimento_id=tipo_movimento_id,
                quantidade=quantidade,
                data_hora=datetime.now(),
                funcionario_id=funcionario_id,
                ordem_servico_id=os_id,
                observacao=observacao,
            )
        )
        estoque_dao.ajustar_quantidade(produto_variacao_id, local_id, delta)
        return novo_movimento_id

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
        for idx, variacao_id in enumerate(variacoes_ids):
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

            quantidade = Decimal(f"{random.uniform(5, 20):.2f}")
            mov_id = cls.registrar_movimento(
                produto_variacao_id=variacao_id,
                local_id=local_id,
                quantidade=quantidade,
                tipo_movimento_id=tipo_movimentos["entrada"],
                funcionario_id=random.choice(funcionarios_ids),
                os_id=random.choice(os_ids) if os_ids else None,
                observacao="Carga inicial",
            )

            if os_ids:
                DAOInstance.get_movimento_estoque_dao().atualizar_data_e_os(
                    mov_id=mov_id,
                    data_hora=datetime(2025, 10, random.randint(1, 30), random.randint(7, 18), random.randint(0, 59)),
                    os_id=random.choice(os_ids),
                )

            if idx < 3:
                mov_saida = cls.registrar_movimento(
                    produto_variacao_id=variacao_id,
                    local_id=local_id,
                    quantidade=min(quantidade, max(Decimal("1"), quantidade - ponto_reposicao + Decimal("1"))),
                    tipo_movimento_id=tipo_movimentos["saida"],
                    funcionario_id=random.choice(funcionarios_ids),
                    os_id=random.choice(os_ids) if os_ids else None,
                    observacao="Reducao proposital para teste",
                )
                if os_ids:
                    DAOInstance.get_movimento_estoque_dao().atualizar_data_e_os(
                        mov_id=mov_saida,
                        data_hora=datetime(2025, 10, random.randint(1, 30), random.randint(7, 18), random.randint(0, 59)),
                        os_id=random.choice(os_ids),
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
            mov_id = cls.registrar_movimento(
                produto_variacao_id=variacao_id,
                local_id=local_id,
                quantidade=Decimal(f"{random.uniform(1, 5):.2f}"),
                tipo_movimento_id=random.choice([tipo_movimentos["saida"], tipo_movimentos["ajuste"]]),
                funcionario_id=random.choice(funcionarios_ids),
                os_id=random.choice(os_ids) if os_ids else None,
                observacao="Movimento automatizado",
            )

            if os_ids:
                DAOInstance.get_movimento_estoque_dao().atualizar_data_e_os(
                    mov_id=mov_id,
                    data_hora=datetime(2025, 10, random.randint(1, 30), random.randint(7, 18), random.randint(0, 59)),
                    os_id=random.choice(os_ids),
                )

    @classmethod
    def atualizar_status_os(
        cls,
        os_id: int,
        novo_status_id: int,
        funcionario_id: int,
        descricao: str,
        inicio_atendimento: Optional[datetime] = None,
        fim_atendimento: Optional[datetime] = None,
    ) -> None:
        os_dao = DAOInstance.get_ordem_servico_dao()
        andamento_dao = DAOInstance.get_andamento_ordem_servico_dao()
        os_atual = os_dao.find_by_id(os_id)
        status_anterior = os_atual.status_id if os_atual else None

        os_dao.update_status(os_id, novo_status_id)
        andamento_dao.insert(
            AndamentoOrdemServico(
                os_id=os_id,
                data_hora=datetime.now(),
                status_anterior_id=status_anterior,
                status_novo_id=novo_status_id,
                funcionario_id=funcionario_id,
                descricao=descricao,
                inicio_atendimento=inicio_atendimento,
                fim_atendimento=fim_atendimento,
            )
        )

    @classmethod
    def seed_tipos_os(cls) -> list[int]:
        descricoes = ["Manutencao eletrica", "Manutencao hidraulica", "Infraestrutura", "TI"]
        tipo_os_dao = DAOInstance.get_tipo_ordem_servico_dao()
        return [tipo_os_dao.insert(TipoOrdemServico(descricao=desc)) for desc in descricoes]

    @classmethod
    def seed_status_os(cls) -> dict[str, int]:
        descricoes = ["aberta", "em_atendimento", "aguardando_material", "concluída", "cancelada"]
        status_dao = DAOInstance.get_status_ordem_servico_dao()
        return {desc: status_dao.insert(StatusOrdemServico(descricao=desc)) for desc in descricoes}

    @classmethod
    def seed_ordens_servico(
        cls,
        solicitantes_ids: list[int],
        areas_ids: list[int],
        tipos_os_ids: list[int],
        equipes_ids: list[int],
        lideres_ids: list[int],
        variacoes_ids: list[int],
        status_map: dict[str, int],
        total: int = 5,
    ) -> list[int]:
        os_ids = []
        base_data = datetime(2025, 10, 10, 9, 0)
        os_dao = DAOInstance.get_ordem_servico_dao()
        item_dao = DAOInstance.get_item_ordem_servico_dao()
        andamento_dao = DAOInstance.get_andamento_ordem_servico_dao()
        for idx in range(total):
            itens = []
            abertura = base_data + timedelta(days=random.randint(-5, 5), hours=random.randint(0, 6))
            previsao = abertura.date() + timedelta(days=random.randint(2, 10))
            for variacao_id in random.sample(variacoes_ids, random.randint(1, 3)):
                itens.append(
                    {
                        "produto_variacao_id": variacao_id,
                        "quantidade_prevista": Decimal(f"{random.uniform(1, 4):.1f}"),
                        "quantidade_usada": None,
                    }
                )

            os_id = os_dao.insert(
                OrdemServico(
                    numero_sequencial=f"OS-{idx + 1:04d}",
                    solicitante_id=random.choice(solicitantes_ids),
                    area_campus_id=random.choice(areas_ids),
                    tipo_os_id=random.choice(tipos_os_ids),
                    equipe_id=random.choice(equipes_ids),
                    lider_id=random.choice(lideres_ids),
                    status_id=status_map["aberta"],
                    prioridade=random.randint(1, 5),
                    data_abertura=abertura,
                    data_prevista=datetime.combine(previsao, datetime.min.time()),
                    descricao_problema=cls.__fake.sentence(nb_words=12),
                )
            )

            for item in itens:
                item_dao.insert(
                    ItemOrdemServico(
                        os_id=os_id,
                        produto_variacao_id=item["produto_variacao_id"],
                        quantidade_prevista=item["quantidade_prevista"],
                        quantidade_usada=item["quantidade_usada"],
                    )
                )

            andamento_dao.insert(
                AndamentoOrdemServico(
                    os_id=os_id,
                    data_hora=abertura,
                    status_anterior_id=None,
                    status_novo_id=status_map["aberta"],
                    funcionario_id=random.choice(lideres_ids),
                    descricao="Abertura da OS",
                )
            )

            os_ids.append(os_id)
        return os_ids

    @classmethod
    def seed_andamentos(cls, ordens_ids: list[int], status_map: dict[str, int], lideres_ids: list[int]) -> None:
        ciclo_status = ["em_atendimento", "aguardando_material", "aberta", "concluída", "concluída"]
        for idx, os_id in enumerate(ordens_ids):
            alvo = ciclo_status[idx % len(ciclo_status)]
            lider = random.choice(lideres_ids)
            if alvo != "aberta":
                cls.atualizar_status_os(
                    os_id=os_id,
                    novo_status_id=status_map[alvo],
                    funcionario_id=lider,
                    descricao="Atualizacao automatica",
                    inicio_atendimento=datetime.now() - timedelta(days=1),
                    fim_atendimento=datetime.now() if alvo == "concluída" else None,
                )

            if idx == 0:
                cls.atualizar_status_os(
                    os_id=os_id,
                    novo_status_id=status_map["aguardando_material"],
                    funcionario_id=lider,
                    descricao="Aguardando material para compra",
                    inicio_atendimento=datetime.now() - timedelta(hours=3),
                    fim_atendimento=None,
                )

                cls.atualizar_status_os(
                    os_id=os_id,
                    novo_status_id=status_map["em_atendimento"],
                    funcionario_id=lider,
                    descricao="Retomado atendimento",
                    inicio_atendimento=datetime.now() - timedelta(hours=1),
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
            status_map=status_os,
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
