from src import data_loader, run_exploration, run_scrubbing
from sqlalchemy import create_engine


df_raw = data_loader()
df_exploration = run_exploration(df_raw)
df_scrubbing = run_scrubbing(df_raw)


engine = create_engine

df_processed = df_scrubbing
df_processed.to_csv(
    "data/processed/db_processed.csv",
    index=False,
    encoding="utf-8-sig"
)


df_processed.to_sql(
    name="fact_health_metrics",
    con=engine,
    index=False,
)


print("\n |          Banco importado com sucesso!       |\n")
