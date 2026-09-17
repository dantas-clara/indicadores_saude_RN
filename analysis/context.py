import pandas as pd
import matplotlib.pyplot as plt


# todo Taxa de Envelhecimento Humano POR SEXO

def tx_envelhecimento_sexo(df):

    df_envelhecimento = df[
        df["id_indicador"] == "dem_01"
    ].copy()

    df_envelhecimento = df_envelhecimento[
        df_envelhecimento["sexo"].isin(["H", "M"])
    ]

    tabela1 = df_envelhecimento.pivot_table(
        index="localidade",
        columns="sexo",
        values="quantitativo",
        aggfunc="sum"
    )

    local = ["RN", "NE", "Brasil"]
    tabela1 = tabela1.reindex([loc for loc in local if loc in tabela1.index])
    tabela1 = tabela1.rename(columns={"H": "Homens", "M": "Mulheres"})

    fig, ax = plt.subplots(figsize=(9, 6))

    tabela1.plot(
    kind="bar",
    ax=ax,
    width=0.45,
    color= ["#2b5c8f", "#d95f02"]

    )

    ax.set_title(
        "Índice de Envelhecimento segundo Sexo e Localidade — 2022",
        fontsize="13",
        fontweight="bold",
        pad=20,
        loc="center",
        x=0.55
    )


    plt.xlabel("Localidade", fontsize=10, labelpad=10)
    plt.ylabel(
         "Índice de pessoas com 60+ para cada 100 pessoas de 0–14 anos",
        fontsize=9.5,
        labelpad=20
    )

    plt.xticks(rotation=0)

    plt.legend(
        title="sexo",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        frameon=True
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.grid(axis='y', linestyle='--',alpha=0.3)



    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f",
            padding=6,
            fontsize="10",
            fontweight="bold",
        )

    ax.set_ylim(0, tabela1.values.max() * 1.20)

    fig.text(
        0.90, 0.02,
        "Python • Matplotlib • PyCharm",
        fontsize=8,
        color="gray",
        ha="right",
        va="bottom"
    )

    plt.tight_layout()
    plt.show()

    return tabela1




# todo Taxa de Envelhecimento Humano POR RAÇA

def tx_envelhecimento_raca(df):

    df_envelhecimento = df[
        (df["id_indicador"] == "dem_01") &
        (df["sexo"] == "total_populacao") &
        (df["raca"].isin(["Branca", "Preta"]))
    ].copy()

    df_envelhecimento["quantitativo"] = pd.to_numeric(
        df_envelhecimento["quantitativo"],
        errors="coerce"
    )

    tabela1 = df_envelhecimento.pivot_table(
        index="localidade",
        columns="raca",
        values="quantitativo",
        aggfunc="sum"
    )

    local = ["RN", "NE", "Brasil"]
    tabela1 = tabela1.reindex([loc for loc in local if loc in tabela1.index])
    tabela1 = tabela1.rename(columns={
        "Branca": "Branca",
        "Preta": "Preta"
    })

    fig, ax = plt.subplots(figsize=(9, 6))

    tabela1.plot(
    kind="bar",
    ax=ax,
    width=0.45,
    color= ["#7B2CBF", "#E76F51"]

    )

    ax.set_title(
        "Índice de Envelhecimento segundo Raça e Localidade — 2022",
        fontsize="13",
        fontweight="bold",
        pad=20,
        loc="center",
        x=0.55
    )


    plt.xlabel("Localidade", fontsize=10, labelpad=10)
    plt.ylabel(
         "Índice de pessoas com 60+ para cada 100 pessoas de 0–14 anos",
        fontsize=9.5,
        labelpad=20
    )

    plt.xticks(rotation=0)

    plt.legend(
        title="Raça",
        bbox_to_anchor=(1.02, 1),
        loc="upper left",
        frameon=True
    )

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.grid(axis='y', linestyle='--',alpha=0.3)



    for container in ax.containers:
        ax.bar_label(
            container,
            fmt="%.1f",
            padding=6,
            fontsize="10",
            fontweight="bold",
        )

    ax.set_ylim(0, tabela1.values.max() * 1.20)

    fig.text(
        0.90, 0.02,
        "Python • Matplotlib • PyCharm",
        fontsize=8,
        color="gray",
        ha="right",
        va="bottom"
    )

    plt.tight_layout()
    plt.show()

    return tabela1















