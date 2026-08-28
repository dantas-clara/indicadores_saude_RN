import pandas as pd


def data_loader():

    df = pd.read_csv('data/raw/indicadores_cuidado.csv')

    return df

