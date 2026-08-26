from src import data_loader_function
from src import show_head, show_tail, show_shape, show_info, show_isna, show_duplicated, show_nunique

df_raw = data_loader_function()

#1 todo HEAD()
print("\n |     HEAD     |\n")
df_show_head = show_head(df_raw)
print(df_show_head)

#2 todo TAIL()
print("\n |     TAIL     |\n")
df_show_tail = show_tail(df_raw)
print(df_show_tail)

#3 todo SHAPE
print("\n |     SHAPE     |\n")
df_show_shape = show_shape(df_raw)
print(df_show_shape)

#4 todo INFO
print("\n |     INFO     |\n")
df_show_info = show_info(df_raw)
print(df_show_info)

#4 todo ISNA
print("\n |     ISNA     |\n")
df_show_isna = show_isna(df_raw).sum()
print(df_show_isna)

#5 todo DUPLICATED
print("\n |     DUPLICATE     |\n")
df_show_duplicated = show_duplicated(df_raw).sum()
print(df_show_duplicated)

#6 todo NUNIQUE
print("\n |     NUNIQUE     |\n")
df_show_nunique = show_nunique(df_raw)
print(df_show_nunique)














