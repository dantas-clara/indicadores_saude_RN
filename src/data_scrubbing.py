def rename_columns(df):
    return df.rename(columns={
        "ID_Indicador": "id_indicador",
        "Nome_Indicador": "nome_indicador",
        "Dimensão_PNaC" : "dimensao_pnac",
        "Ano" : "ano",
        "Localidade" : "localidade",
        "Sexo" : "sexo",
        "Raça" : "raca",
        "Faixa Etaria" : "faixa_etaria",
        "Tipo de Arranjo Familiar" : "tipo_arranjo_familiar",
        "Renda" : "renda",
        "Valor" : "valor",
        "Quantitativo" : "quantitativo"
    })


def replace_sings(df):
    return df.replace({
        "quantitativo" : {
            ",": ".",
            "%": ""
        }
    }, regex=True)



def fill_name(df):
    return df.fillna({
        "ano": "2022",
        "sexo" : "total_populacao",
        "dimensao_pnac": "Contexto",
        "localidade": "Brasil",
        "valor": "Percentual"
    })


def astype_data(df):
    return df.astype({
        "ano" : "int64",
        "quantitativo" : "float64"
    })

def sort_data(df):
    return df.sort_values(["ano"])



def run_scrubbing(df):
    print("\n|    RENAME       |\n")
    df_show_rename = rename_columns(df)
    print(df_show_rename.info())


    print("\n|    REPLACE       |\n")
    df_show_replace = replace_sings(df_show_rename)
    print(df_show_replace)
    print("\n|    CONFIRMAÇÃO DA EXECUÇÃO DO REPLACE       |\n")
    print(df_show_replace.astype(str).apply(lambda col: col.str.contains(",").any()))
    print(df_show_replace.astype(str).apply(lambda col: col.str.contains("%").any()))


    print("\n|   TODAS AS COLUNAS ANTES DO MÉTODO FILLNA     |\n")
    print(df_show_replace.isna().sum())


    print("\n|     FILLNA     |\n")
    df_show_fillna = fill_name(df_show_replace)
    print("\n|     FILLNA COLUNA: SEXO    |\n")
    print(df_show_fillna["sexo"].unique())
    print("\n|    CONFIRMAÇÃO DA EXECUÇÃO DO FILLNA     |\n")
    print(df_show_fillna[["dimensao_pnac", "ano", "localidade", "valor"]].isna().any())

    print("\n|   TODAS AS COLUNAS APÓS O MÉTODO FILLNA     |\n")
    print(df_show_fillna.isna().sum())



    print("\n|    ASTYPE      |\n")
    df_show_astype = astype_data(df_show_fillna)
    print(df_show_astype["ano"].unique())

    print("\n|    SORT_VALUES     |\n")
    df_show_sort = sort_data(df_show_astype)
    print(df_show_sort["ano"].unique())

    return df_show_sort




