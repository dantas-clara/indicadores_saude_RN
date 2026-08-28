from src import data_loader_function
from src import run_exploration
from src import run_scrubbing

df_raw = data_loader_function()
df_exploration = run_exploration(df_raw)
df_scrubbing = run_scrubbing(df_raw)


df_processed = df_scrubbing
df_processed.to_csv(
    "data/processed/db_processed.csv",
    index=False,
    encoding="utf-8-sig"
)


