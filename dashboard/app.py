import streamlit as st
import pandas as pd
import plotly.express as px

from src.connection import get_engine

st.set_page_config(
    page_title="Índice de Envelhecimento",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard: Índice de Envelhecimento")

st.write(
    "Número de pessoas com 60 anos ou mais "
    "para cada grupo de 100 pessoas de 0 a 14 anos de idade."
)

@st.cache_data(ttl=600)
def data_loader():
    db_engine = get_engine()

    query = """
            SELECT ano, 
                   sexo, 
                   localidade, 
                   raca, 
                   `Índice` AS indice
            FROM view_envelhecimento
            ORDER BY ano, localidade;
            """

    df = pd.read_sql(query, db_engine)

    df["indice"] = pd.to_numeric(df["indice"], errors="coerce").fillna(0).astype(float)

    df["sexo"] = df["sexo"].astype(str).str.strip()
    df["raca"] = df["raca"].astype(str).str.strip()
    df["localidade"] = df["localidade"].astype(str).str.strip()

    return df

try:
    df = data_loader()

    st.sidebar.header("🔍 Filtros")

    anos_disponiveis = sorted(df["ano"].unique().tolist())
    ano_selecionado = st.sidebar.multiselect(
        "Ano",
        options=anos_disponiveis,
        default=anos_disponiveis
    )

    locais_disponiveis = sorted(df["localidade"].unique().tolist())
    locais_selecionados = st.sidebar.multiselect(
        "Localidade",
        options=locais_disponiveis,
        default=locais_disponiveis
    )

    df_filtro = df[
        (df["ano"].isin(ano_selecionado)) &
        (df["localidade"].isin(locais_selecionados))
    ]

    st.divider()

    col_graf1, col_graf2 = st.columns(2)

    with col_graf1:
        st.subheader("Índice de Envelhecimento por Sexo")

        df_sexo = df_filtro[df_filtro["sexo"].str.upper().isin(["H", "M"])].copy()

        if not df_sexo.empty:
            df_sexo_agrupado = df_sexo.groupby(["localidade", "sexo"], as_index=False)["indice"].mean()
            df_sexo_agrupado["sexo_nome"] = df_sexo_agrupado["sexo"].str.upper().map({"H": "Homens", "M": "Mulheres"})

            fig_sexo = px.bar(
                df_sexo_agrupado,
                x="localidade",
                y="indice",
                color="sexo_nome",
                barmode="group",
                text_auto=".1f",
                color_discrete_map={"Homens": "#2b5c8f", "Mulheres": "#d95f02"},
                labels={"localidade": "Localidade", "indice": "Índice de Envelhecimento", "sexo_nome": "Sexo"}
            )
            fig_sexo.update_layout(
                xaxis={"categoryorder": "array", "categoryarray": ["RN", "NE", "Brasil"]},
                yaxis_title="Índice (60+ por 100 de 0-14)"
            )
            st.plotly_chart(fig_sexo, use_container_width=True)
        else:
            st.warning("Sem registros para Sexo H/M no filtro atual.")


    with col_graf2:
        st.subheader("Índice de Envelhecimento por Raça")

        df_raca = df_filtro[
            (df_filtro["sexo"].str.lower() == "total_populacao") &
            (df_filtro["raca"].str.capitalize().isin(["Branca", "Preta"]))
        ].copy()

        df_raca["raca_nome"] = df_raca["raca"].str.capitalize()

        if not df_raca.empty:
            df_raca_agrupado = df_raca.groupby(["localidade", "raca_nome"], as_index=False)["indice"].mean()

            fig_raca = px.bar(
                df_raca_agrupado,
                x="localidade",
                y="indice",
                color="raca_nome",
                barmode="group",
                text_auto=".1f",
                color_discrete_map={"Branca": "#7B2CBF", "Preta": "#E76F51"},
                labels={"localidade": "Localidade", "indice": "Índice de Envelhecimento", "raca_nome": "Raça"}
            )
            fig_raca.update_layout(
                xaxis={"categoryorder": "array", "categoryarray": ["RN", "NE", "Brasil"]},
                yaxis_title="Índice (60+ por 100 de 0-14)"
            )
            st.plotly_chart(fig_raca, use_container_width=True)
        else:
            st.warning("Sem registros para Raça (total_populacao + Branca/Preta) no filtro atual.")


    with st.expander("📄 Ver dados detalhados da tabela"):
        st.dataframe(df_filtro, use_container_width=True)

except Exception as e:
    st.error("Erro ao carregar dados do MySQL:")
    st.exception(e)