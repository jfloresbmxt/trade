import streamlit as st
from polars import read_parquet, col
from secciones.estatal.detalle import detalle_empresas

@st.cache_data
def get_list():
    estados = read_parquet("data/lista_estados.parquet")
    estados = estados.to_series().to_list()

    return estados

@st.cache_data
def get_states_data(state):
    df_detail = read_parquet("data/detalle/" + state + ".parquet")
    subsector = (
        df_detail.select(col("Título"))
        .unique()
        .select(col("Título")
        .apply(lambda x: x.replace("T",""))
        .apply(lambda x: x.strip())
        )
        ).to_series().to_list()

    return [df_detail, subsector]

st.subheader("Detalle de empresas")

col1, col2 = st.columns(2)
with col1:
    opcion = st.selectbox("seleccionar estado", get_list())
    df_detail, subsector = get_states_data(opcion)
with col2:
    opcion2 = st.selectbox("Seleccionar subsector", subsector)


detalle_empresas(df_detail, opcion2)
