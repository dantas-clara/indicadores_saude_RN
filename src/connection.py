from sqlalchemy import create_engine


def get_engine(df):
    engine = create_engine(
        "mysql+pymysql://[...]"
    )

    df.to_csv(
        "data/processed/db_processed.csv",
        index=False,
        encoding="utf-8-sig"
    )

    df.to_sql(
        name="fact_health_metrics",
        con=engine,
        index=False,
    )

    print("\n\n |          Banco importado com sucesso!       |\n")

