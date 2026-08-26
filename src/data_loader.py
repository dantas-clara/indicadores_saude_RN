import pandas as pd


def data_loader_function():

    df = pd.read_csv('data/raw/indicadores_cuidado.csv')

    return df

