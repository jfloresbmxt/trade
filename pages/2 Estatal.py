import streamlit as st
from css.metrics import metrics
from polars import read_parquet, col
from graphs.across_time import gen_graphs
import geopandas as gpd
from streamlit_folium import st_folium
from graphs.maps.gen_maps import gen_maps

st.title('Información Estatal')


def statistics(df):
    a = df["fraccion"].n_unique()
    b = df["subsector"].n_unique()
    c = df["rfc_e"].n_unique()


    df = (df.groupby(["mes"]).agg(
        col("val_usd").sum(),
        col("rfc_e").n_unique()
        ))
    
    d = format(int(df["val_usd"].sum() / 1000000), ',d')
    f = format(int(df["val_usd"].mean()/ 1000000), ',d')
    g = format(int(df["rfc_e"].mean()), ',d')
    
    return [a, b, c, d, f, g, df]

@st.cache_data
def get_list():
    df = read_parquet("data/lista_estados.parquet")
    df = df.to_series().to_list()

    return df

@st.cache_data
def get_states_data(state):
    stats = read_parquet("data/summary/stats.parquet")
    stats = stats.filter(col("estado") == state)

    a = format(int(stats["products"][0]), ",d")
    b = format(int(stats["sectors"][0]), ",d")
    c = format(int(stats["companies"][0]), ",d")
    d = format(int(stats["exp_tot"][0]), ",d")
    e = format(int(stats["exp_prom"][0]), ",d")
    f = format(int(stats["comp_prom"][0]), ",d")

    time = read_parquet("data/summary/time.parquet")
    time = time.filter(col("estado") == state)

    return [a,b,c,d,e,f, time]

@st.cache_data
def plot_map(state):
    s = gpd.read_parquet("data/map_info/state_" + state + ".parquet")
    map_info = gpd.read_parquet("data/map_info/cp_" + state + ".parquet")
    
    return [s, map_info]


estados = get_list()

estado = st.sidebar.selectbox(
    "Selecciona estado",
    estados
)

a, b, c, d, e, f, time = get_states_data(estado)

st.subheader(f"Informacion de {estado}")
col1, col2, col3 = st.columns(3)
col1.markdown(metrics("Productos", a, "fas fa-globe-americas"), unsafe_allow_html=True)
col2.markdown(metrics("Sectores", b, "fas fa-cogs"), unsafe_allow_html=True)
col3.markdown(metrics("Empresas Totales", c, "fas fa-city"), unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.markdown(metrics("Exportaciones totales", d + "M", "fas fa-globe-americas"), unsafe_allow_html=True)
col2.markdown(metrics("Exportaciones promedio", e + " M", "fas fa-globe-americas"), unsafe_allow_html=True)
col3.markdown(metrics("Empresas mensuales promedio", f, "fas fa-globe-americas"), unsafe_allow_html=True)


st.header("Comportamiento Exportaciones")
option = st.selectbox(
    'Selecciona la variable',
    ('Exportaciones', 'Numero_empresas'))

def exp_section():
    fig = gen_graphs(time, option)
    df = gen_graphs(time, "tabla")
    tab1, tab2 = st.tabs(["Gráfica", "Datos"])

    with tab1:
        # Plot!
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </>
                    """
        
        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # Table
        st.table(df)

exp_section()

st.subheader("Concentración de empresas")

s, map_info = plot_map(estado)

m = gen_maps(s, map_info)

st_data = st_folium(m, width=500)