from load_csv_to_postgres import load_csv_to_postgres
from migrate_pg_to_mongo import migrate_postgres_to_mongodb


def main() -> None:
    """
    Função principal que orquestra o carregamento de dados do Excel para PostgreSQL
    e a posterior migração dos dados do PostgreSQL para o MongoDB.
    """
    print("🚀 Iniciando processo de ETL...\n")

    print("📥 Carregando dados do Excel para o PostgreSQL...")
    load_csv_to_postgres("data/IDH2010.csv")
    print("✅ Dados carregados no PostgreSQL!\n")

    print("🔄 Migrando dados do PostgreSQL para o MongoDB...")
    migrate_postgres_to_mongodb()
    print("✅ Dados migrados com sucesso para o MongoDB!\n")

    print("🏁 Processo concluído com sucesso.")


if __name__ == "__main__":
    main()
