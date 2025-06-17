# Projeto ETL PostgreSQL → MongoDB

Este projeto tem como objetivo demonstrar o fluxo de dados entre bancos relacionais e NoSQL, utilizando como exemplo o carregamento de dados de um arquivo Excel para o PostgreSQL e a migração desses dados para o MongoDB.

## Estrutura do projeto

```
projeto_nosql_puc/
├── data/
│ └── IDH2010.xlsx
├── docker-compose.yml # Orquestração dos containers
├── src/
│ ├── load_excel_to_postgres.py
│ ├── migrate_pg_to_mongo.py 
│ └── main.py
├── .env
├── requirements.txt
└── README.md
````


## Pré-requisitos

- Docker e Docker Compose instalados
- Python 3.12+
- Acesso ao terminal/bash

## Configuração

### 1. Crie o arquivo `.env` na raiz do projeto com o seguinte conteúdo (ajuste conforme necessidade):

```
POSTGRES_USER=admin
POSTGRES_PASSWORD=admin123
POSTGRES_DB=mydatabase
POSTGRES_PORT=5432

MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=root123
MONGO_PORT=27017
```

### 2. Inicie os containers:

```
docker-compose up -d
```
### 3. Instale as dependências Python:

```
pip install -r requirements.txt
```

O script irá:

1. Ler o arquivo Excel e carregar os dados no PostgreSQL

2. Migrar os dados do PostgreSQL para o MongoDB


### 4 Executar o ETL completo

No diretório raiz do projeto, rode:

```
python src/main.py
```

### 5. Verificar os dados no MongoDB

Você pode conectar ao MongoDB na porta definida no .env (default: 27017) usando o cliente de sua preferência (Mongo Shell, Compass, etc.) e checar a coleção indicadores_municipais no banco indicadores_db.


## Tecnologias utilizadas

- PostgreSQL 16

- MongoDB 6.0

- Python (pandas, SQLAlchemy, pymongo, dotenv)

- Docker & Docker Compose