def get_999(df):
    return df.isin(["999", 999]).sum()

def get_head (df):
    return df.head()

def get_tail (df):
    return df.tail()

def get_shape(df):
    return df.shape

def get_info(df):
    return df.info()

def get_isna(df):
    return df.isna()

def get_missing_percentage(df):
    return (df.isnull().sum() / len (df) * 100).round(2)

def get_duplicated(df):
    return df.duplicated()

def get_nunique(df):
    return df.nunique()

def get_unique(coluna):
    return coluna.unique()


def run_exploration(df):
    print("\n |     ISIN     |\n")
    df_show_999 = get_999(df)
    print(df_show_999)

    # 1 todo HEAD()
    print("\n |     HEAD     |\n")
    df_show_head = get_head(df)
    print(df_show_head)

    # 2 todo TAIL()
    print("\n |     TAIL     |\n")
    df_show_tail = get_tail(df)
    print(df_show_tail)

    # 3 todo SHAPE
    print("\n |     SHAPE     |\n")
    df_show_shape = get_shape(df)
    print(df_show_shape)

    # 4 todo INFO
    print("\n |     INFO     |\n")
    df_show_info = get_info(df)
    print(df_show_info)

    # 4.1 todo ISNA
    print("\n |     ISNA     |\n")
    df_show_isna = get_isna(df).sum()
    print(df_show_isna)

    # 4.2 todo ISNULL PERCENTAGE
    print("\n |     ISNULL PERCENTAGE    |\n")
    df_show_isnull = get_missing_percentage(df)
    print(df_show_isnull)

    # 5 todo DUPLICATED
    print("\n |     DUPLICATE     |\n")
    df_show_duplicated = get_duplicated(df).sum()
    print(df_show_duplicated)

    # 6 todo NUNIQUE
    print("\n |     NUNIQUE     |\n")
    df_show_nunique = get_nunique(df)
    print(df_show_nunique)

    # 7 todo UNIQUE
    print("\n |     UNIQUE     |\n")
    df_show_unique = get_unique(df["Ano"])
    print(df_show_unique)

