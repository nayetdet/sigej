## SIGEJ – Sistema de Gestão de Jardinagem e Manutenção

Sistema web para controle de ordens de serviço, equipes de manutenção e estoque de materiais de jardinagem e manutenção do IFCE Campus Maracanaú.

O foco do projeto é o **modelo relacional** e o uso de **SQL explícito** (sem ORM), atendendo aos requisitos da disciplina de Banco de Dados.

---

## Principais funcionalidades

- Cadastro de solicitantes, áreas do campus, tipos de área, setores e status de OS.
- Cadastro de funcionários, tipos de funcionário, equipes de manutenção e membros de equipe.
- Catálogo de materiais: categorias, unidades, marcas, cores, tamanhos, produtos e variações.
- Gestão de estoque:
  - Locais de estoque (depósitos) com responsável.
  - Movimentos de entrada, saída e ajuste.
  - Controle de ponto de reposição por variação/local.
- Ordens de Serviço (OS):
  - Abertura de OS com número sequencial, prioridade, área, tipo, equipe e líder.
  - Itens de OS com quantidades prevista e usada.
  - Andamentos com histórico de mudanças de status.
- Dashboard inicial com:
  - OS em aberto por prioridade e área.
  - Materiais abaixo do ponto de reposição.
  - Timeline da última OS.
  - Consumo de materiais por equipe em um período.
  - OS concluídas por tipo no ano.

---

## Tecnologias

- **Linguagem:** Python 3 (>= 3.13).
- **Framework web:** [Flask](https://flask.palletsprojects.com/).
- **Banco de dados:** PostgreSQL.
- **Acesso a dados:** SQL manual com [psycopg](https://www.psycopg.org/) (sem ORM).
- **Geração de dados de teste:** [Faker](https://faker.readthedocs.io/).
- **Gerenciador de ambientes/depêndencias:** [uv](https://github.com/astral-sh/uv).
- **Docker:** `docker-compose.yml` para subir um PostgreSQL de desenvolvimento.

Estrutura em camadas:

- `src/sigej/routes` – rotas Flask (controllers).
- `src/sigej/services` – regras de negócio.
- `src/sigej/daos` – DAOs com SQL explícito.
- `resources/templates` – templates HTML.
- `resources/static` – assets estáticos (CSS, favicon).
- `scripts/sql/schema.sql` – criação de todas as tabelas.
- `scripts/seed.py` – popular o banco com dados realistas.

---

## Requisitos

- Python 3.13+ (ou compatível com o `pyproject.toml`).
- PostgreSQL 15+ (local ou via Docker).
- `uv` instalado globalmente (recomendado).
- Docker (opcional, para subir o banco rapidamente).

---

## Configuração do ambiente

1. **Clonar o repositório**

```bash
git clone https://github.com/nayetdet/sigej.git
cd sigej
```

2. **Configurar variáveis de ambiente**

Use o exemplo fornecido:

```bash
cp .env.example .env
```

Edite `.env` e ajuste se necessário:

- `FLASK_SECRET_KEY`
- `DATABASE_HOST`
- `DATABASE_PORT`
- `DATABASE_NAME`
- `DATABASE_USERNAME`
- `DATABASE_PASSWORD`

3. **Subir o PostgreSQL com Docker (opcional, mas recomendado)**

```bash
docker compose up -d
```

O serviço `postgres` vai subir na porta `5432` usando as credenciais definidas no `.env`.

4. **Instalar dependências com uv**

```bash
make install
```

Esse comando executa `uv sync --all-groups` com base no `pyproject.toml`.

---

## Banco de dados

### Criar o schema

Crie o banco configurado em `.env` (por padrão, `sigej`) e execute:

```bash
psql -h localhost -U postgres -d sigej -f scripts/sql/schema.sql
```

> Ajuste host, usuário e nome do banco conforme o seu `.env`.

### Popular com dados de exemplo

O projeto inclui um seed que gera:

- pessoas, funcionários, tipos de funcionário, setores;
- áreas e tipos de área;
- equipes, membros e líderes;
- categorias, unidades, marcas, cores, tamanhos, produtos e variações;
- locais de estoque, movimentos de entrada/saída/ajuste;
- ordens de serviço, itens de OS e andamentos;
- dados coerentes para os relatórios obrigatórios.

Execute:

```bash
make seed
```

---

## Execução da aplicação

Com o ambiente configurado e o banco pronto:

```bash
make run
```

ou, equivalentemente:

```bash
uv run python -m src.sigej.main
```

A aplicação ficará disponível em:

```text
http://localhost:5000
```

---

## Consultas e relatórios SQL

As consultas obrigatórias da disciplina são implementadas como SQL puro nos DAOs, e também estão documentadas no relatório em LaTeX (`relatorio_sigej.tex`):

1. **Ordens de serviço em aberto por prioridade e área**
2. **Materiais abaixo do ponto de reposição**
3. **Timeline de uma OS**
4. **Consumo por equipe em um período**
5. **OS concluídas por tipo no ano**

> Não é utilizado nenhum ORM (Hibernate, Django ORM, Sequelize, etc.). Todas as consultas são escritas manualmente.

---

## Relatórios e documentação

- **DER:** `docs/results/diagrams/der.png`
- **Screenshots do sistema:** `docs/results/screenshots/`
- **Relatório em LaTeX:** `relatorio_sigej.tex`
  - Para gerar o PDF (com LaTeX instalado):
    ```bash
    pdflatex relatorio_sigej.tex
    ```

Opcionalmente, há um script de geração de PDF via Python (resumo do relatório + imagens), usando `fpdf2`:

```bash
uv run python scripts/generate_report.py
# Gera docs/sigej_relatorio.pdf
```

---

## Estrutura resumida de pastas

```text
.
├── docker-compose.yml         # Serviço PostgreSQL de desenvolvimento
├── Makefile                   # Comandos de atalho (install/run/seed)
├── pyproject.toml             # Metadados e dependências Python
├── relatorio_sigej.tex        # Relatório acadêmico (LaTeX)
├── resources/
│   ├── static/                # CSS e assets
│   └── templates/             # Templates HTML (Flask)
├── scripts/
│   ├── sql/schema.sql         # Criação do schema PostgreSQL
│   ├── seed.py                # Seed de dados de exemplo
│   └── generate_report.py     # Geração de relatório PDF (opcional)
├── src/
│   └── sigej/
│       ├── daos/              # DAOs com SQL explícito
│       ├── models/            # Modelos de domínio (dataclasses simples)
│       ├── routes/            # Rotas Flask
│       ├── services/          # Regras de negócio
│       ├── config.py          # Configuração (usa variáveis de ambiente)
│       └── main.py            # Ponto de entrada da aplicação Flask
└── docs/
    └── results/
        ├── diagrams/der.png   # Diagrama ER
        └── screenshots/       # Prints de telas
```
