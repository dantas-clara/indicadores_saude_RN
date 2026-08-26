from src import data_loader_function
from src import (get_999,
                 get_head,
                 get_tail,
                 get_shape,
                 get_info,
                 get_isna,
                 get_missing_percentage,
                 get_duplicated,
                 get_nunique,
                 get_unique)

df_raw = data_loader_function()


print("\n |     ISIN     |\n")
df_show_999 = get_999(df_raw)
print(df_show_999)

#1 todo HEAD()
print("\n |     HEAD     |\n")
df_show_head = get_head(df_raw)
print(df_show_head)

#2 todo TAIL()
print("\n |     TAIL     |\n")
df_show_tail = get_tail(df_raw)
print(df_show_tail)

#3 todo SHAPE
print("\n |     SHAPE     |\n")
df_show_shape = get_shape(df_raw)
print(df_show_shape)

#4 todo INFO
print("\n |     INFO     |\n")
df_show_info = get_info(df_raw)
print(df_show_info)

#4.1 todo ISNA
print("\n |     ISNA     |\n")
df_show_isna = get_isna(df_raw).sum()
print(df_show_isna)

#4.2 todo ISNULL PERCENTAGE
print("\n |     ISNULL PERCENTAGE    |\n")
df_show_isnull = get_missing_percentage(df_raw)
print(df_show_isnull)

#5 todo DUPLICATED
print("\n |     DUPLICATE     |\n")
df_show_duplicated = get_duplicated(df_raw).sum()
print(df_show_duplicated)

#6 todo NUNIQUE
print("\n |     NUNIQUE     |\n")
df_show_nunique = get_nunique(df_raw)
print(df_show_nunique)

#7 todo UNIQUE
print("\n |     UNIQUE     |\n")
df_show_unique = get_unique(df_raw["Ano"])
print(df_show_unique)














