import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

def get_postgres_engine() -> object:
    """
    Cria a engine de conexão com o banco PostgreSQL a partir de variáveis de ambiente.

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

def load_csv_to_postgres(file_path: str) -> None:
    """
    Carrega dados de um arquivo CSV para a tabela indicadores_municipais no PostgreSQL.

    Args:
        file_path (str): Caminho para o arquivo CSV.
    """
    df = pd.read_csv(file_path, delimiter=';', decimal=',', encoding='latin1')

    df.columns = [
        "ano",
        "cod_uf",
        "nome_uf",
        "cod_municipio",
        "nome_municipio",
        "expectativa_vida",
        "mortalidade_infantil"
    ]

    df.dropna(subset=["cod_municipio"], inplace=True)

    df["expectativa_vida"] = pd.to_numeric(df["expectativa_vida"], errors='coerce')
    df["mortalidade_infantil"] = pd.to_numeric(df["mortalidade_infantil"], errors='coerce')

    engine = get_postgres_engine()

    df.to_sql(
        name="indicadores_municipais",
        con=engine,
        if_exists="append",
        index=False
    )

    print("✅ Dados carregados com sucesso para o PostgreSQL!")

if __name__ == "__main__":
    load_csv_to_postgres("data/IDH2010.csv")
