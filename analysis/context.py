import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D



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


# todo Taxa de Envelhecimento Humano POR RENDA

def tx_renda(df, localidade="Brasil"):


    grupo_azul = [
        "Acima de 3 SM até 5 SM",
        "Acima de 5 SM até 10 SM",
        "Acima de 10 SM"
    ]

    grupo_laranja = [
        "Acima de 1 SM até 3 SM"
    ]

    grupo_vermelho = [
        "Até a linha administrativa do Bolsa Família",
        "Acima da linha administrativa do Bolsa Família até 1/2 SM",
        "Acima de 1/2 SM até 1 SM"
    ]

    todas_faixas = (
            grupo_azul
            + grupo_laranja
            + grupo_vermelho
    )


    dados_populacao = {
        "Brasil": {
            "Azul": ["19.06 mi", "55.04 mi", "16.92 mi", "15.85 mi", "17.56 mi"],
            "Laranja": ["68.97 mi", "72.18 mi", "71.11 mi", "61.90 mi", "68.11 mi"],
            "Vermelho": ["126.16 mi", "123.16 mi", "126.16 mi", "136.44 mi", "128.73 mi"],
        },
        "NE": {
            "Azul": ["2.18 mi", "2.29 mi", "2.12 mi", "2.02 mi", "1.91 mi"],
            "Laranja": ["10.42 mi", "11.35 mi", "11.08 mi", "8.19 mi", "9.55 mi"],
            "Vermelho": ["41.93 mi", "40.89 mi", "41.38 mi", "44.38 mi", "43.13 mi"],
        },
        "RN": {
            "Azul": ["0.18 mi", "0.17 mi", "0.11 mi", "0.19 mi", "0.11 mi"],
            "Laranja": ["0.78 mi", "0.86 mi", "0.81 mi", "0.58 mi", "0.68 mi"],
            "Vermelho": ["2.32 mi", "2.24 mi", "2.30 mi", "2.49 mi", "2.41 mi"],
        }
    }



    df_renda = df[
        (df["id_indicador"] == "dem_05") &
        (df["localidade"] == localidade) &
        (df["renda"].isin(todas_faixas))
        ].copy()


    tabela = df_renda.pivot_table(
        index="ano",
        columns="renda",
        values="quantitativo",
        aggfunc="sum"
    )



    tabela["Vermelho"] = tabela[grupo_vermelho].sum(axis=1)
    tabela["Laranja"] = tabela[grupo_laranja].sum(axis=1)
    tabela["Azul"] = tabela[grupo_azul].sum(axis=1)

    tabela_grupos = tabela[["Vermelho", "Laranja", "Azul"]]

    print(f"\nDistribuição por grupos de renda — {localidade}:")
    print(tabela_grupos.round(1))


    fig, ax = plt.subplots(figsize=(11.5, 6))

    cores = {
        "Vermelho": "#D62728",
        "Laranja": "#D95F02",
        "Azul": "#2B5C8F"
    }

    anos_str = tabela_grupos.index.astype(str).tolist()

    for grupo in tabela_grupos.columns:

        ax.plot(
            anos_str,
            tabela_grupos[grupo],
            marker="o",
            linewidth=2.5,
            markersize=6,
            label=grupo,
            color=cores[grupo]
        )


        val_final = tabela_grupos[grupo].iloc[-1]

        pop_txt = ""
        if localidade in dados_populacao and grupo in dados_populacao[localidade]:
            pop_txt = f"\n({dados_populacao[localidade][grupo][-1]})"

        ax.annotate(
            f"{val_final:.1f}%{pop_txt}",
            xy=(anos_str[-1], val_final),
            xytext=(8, -3),
            textcoords="offset points",
            fontsize=8.5,
            fontweight="bold",
            color=cores[grupo],
            va="center"
        )



    if localidade == "Brasil":
        val_2019_azul = tabela_grupos.loc[2019, "Azul"] if 2019 in tabela_grupos.index else tabela_grupos.loc[
            "2019", "Azul"]

        ax.annotate(
            "Outlier — desvio de 116,9% (investigação em aberto)",
            xy=("2019", val_2019_azul),
            xytext=("2018.85", val_2019_azul - 2),
            ha="right",
            va="center",
            fontsize=8.5,
            fontweight="bold",
            color=cores["Azul"],
            arrowprops=dict(
                arrowstyle="->",
                color=cores["Azul"],
                lw=1.2,
                connectionstyle="arc3,rad=-0.2"
            )
        )



    fig.suptitle(
        f"Distribuição da Renda Domiciliar — {localidade} (2018–2022)",
        fontsize=13,
        fontweight="bold",
        y=0.98
    )

    plt.xlabel("Ano", fontsize=10, labelpad=10)
    plt.ylabel("Percentual da população (%)", fontsize=10, labelpad=10)


    legenda = [

        Line2D([], [], color=cores["Azul"], linewidth=3, label="AZUL"),
        Line2D([], [], color="none", linewidth=0, label="    Acima de 3 SM até 5 SM"),
        Line2D([], [], color="none", linewidth=0, label="    Acima de 5 SM até 10 SM"),
        Line2D([], [], color="none", linewidth=0, label="    Acima de 10 SM"),


        Line2D([], [], color=cores["Laranja"], linewidth=3, label="LARANJA"),
        Line2D([], [], color="none", linewidth=0, label="    Acima de 1 SM até 3 SM"),


        Line2D([], [], color=cores["Vermelho"], linewidth=3, label="VERMELHO"),
        Line2D([], [], color="none", linewidth=0, label="    Até a linha adm do Bolsa Família"),
        Line2D([], [], color="none", linewidth=0,
               label="    Acima da linha adm do Bolsa Família até 1/2 SM"),
        Line2D([], [], color="none", linewidth=0, label="    Acima de 1/2 SM até 1 SM"),

        Line2D([], [], color="none", label=""),
        Line2D([], [], color="none", label="*SM: Salário Mínimo")
    ]

    leg = ax.legend(
        handles=legenda,
        title="Grupos de Renda",
        bbox_to_anchor=(1.18, 1.0),
        loc="upper left",
        frameon=True,
        facecolor="#F8F9FA",
        edgecolor="#CCCCCC",
        framealpha=0.95,
        handlelength=2.2,
        labelspacing=0.5,
        fontsize=8,
        title_fontsize=9
    )


    leg.get_frame().set_boxstyle("round,pad=0.5,rounding_size=0.4")


    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.grid(axis="y", linestyle="--", alpha=0.3)

    fig.text(
        0.98,
        0.02,
        "Python • Matplotlib • PyCharm",
        fontsize=8,
        color="gray",
        ha="right",
        va="bottom"
    )


    fig.subplots_adjust(right=0.58, top=0.88, bottom=0.12, left=0.08)
    plt.show()

    return tabela_grupos