import os

import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient
from sqlalchemy import create_engine

load_dotenv()


def get_postgres_engine() -> object:
    """
    Cria a engine de conexão com o banco PostgreSQL.

    Returns:
        object: Engine SQLAlchemy para o PostgreSQL.
    """
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = "localhost"
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")

    engine_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return create_engine(engine_url)


def get_mongo_client() -> MongoClient:
    """
    Cria o cliente de conexão com o MongoDB.

    Returns:
        MongoClient: Cliente conectado ao MongoDB.
    """
    user = os.getenv("MONGO_INITDB_ROOT_USERNAME")
    password = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
    host = "localhost"
    port = os.getenv("MONGO_PORT")

    mongo_url = f"mongodb://{user}:{password}@{host}:{port}/"
    return MongoClient(mongo_url)


def migrate_postgres_to_mongodb() -> None:
    """
    Lê os dados do PostgreSQL e insere como documentos no MongoDB.
    """
    engine = get_postgres_engine()
    df = pd.read_sql("SELECT * FROM indicadores_municipais", con=engine)

    client = get_mongo_client()
    db = client["indicadores_db"]
    collection = db["indicadores_municipais"]

    collection.drop()

    records = df.to_dict(orient="records")
    collection.insert_many(records)

    print("✅ Dados migrados com sucesso do PostgreSQL para o MongoDB!")


if __name__ == "__main__":
    migrate_postgres_to_mongodb()
