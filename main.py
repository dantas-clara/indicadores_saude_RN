from src import data_loader_function
from src import run_exploration
from src import run_scrubbing

df_raw = data_loader_function()
df_exploration = run_exploration(df_raw)
df_scrubbing = run_scrubbing(df_raw)




