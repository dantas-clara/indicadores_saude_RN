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

