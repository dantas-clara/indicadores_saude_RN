from src import data_loader, run_exploration, run_scrubbing, get_engine
from analysis import indx_envelhecimento_sexo,  indx_envelhecimento_raca, tx_renda



df_raw = data_loader()
df_exploration = run_exploration(df_raw)
df_scrubbing = run_scrubbing(df_raw)
df_processed = get_engine(df_scrubbing)
df_envelhecimento_sexo = indx_envelhecimento_sexo(df_scrubbing)
df_envelhecimento_raca = indx_envelhecimento_raca(df_scrubbing)
df_renda = tx_renda(df_scrubbing)