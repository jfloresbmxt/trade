import streamlit as st
from streamlit_folium import st_folium
import streamlit_authenticator as stauth
from polars import read_parquet, col
from secciones.estatal.detalle import detalle_empresas
from graphs.maps.gen_maps import gen_maps
import geopandas as gpd
import yaml
from yaml.loader import SafeLoader

with open(".config.yaml") as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login('Autenticate', 'main')

if authentication_status is False:
    st.error('Usuario o contraseña son incorrectos')
if authentication_status is None:
    st.warning('Para ver esta sección, inicia sesion')
if authentication_status:
    authenticator.logout('Cerrar sesión', 'main', key='unique_key')

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

    @st.cache_data
    def plot_map(state):
        s = gpd.read_parquet("data/map_info/state_" + state + ".parquet")
        map_info = gpd.read_parquet("data/map_info/cp_" + state + ".parquet")
        
        return [s, map_info]

    st.subheader("Detalle de empresas")

    col1, col2 = st.columns(2)
    with col1:
        opcion = st.selectbox("seleccionar estado", get_list())
        df_detail, subsector = get_states_data(opcion)
    with col2:
        opcion2 = st.selectbox("Seleccionar subsector", subsector)


    detalle_empresas(df_detail, opcion2)

    st.subheader("Concentración de empresas")

    s, map_info = plot_map(opcion)

    m = gen_maps(s, map_info)

    st_data = st_folium(m, width=500)