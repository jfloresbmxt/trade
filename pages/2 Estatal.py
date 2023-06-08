# import streamlit as st
# from css.metrics import metrics
# from polars import read_parquet, col
# import geopandas as gpd
# from graphs.across_time import gen_graphs
# from streamlit_folium import st_folium
# from graphs.maps.gen_maps import gen_maps

# st.title('Información Estatal')

# def statistics(df):
#     a = df["fraccion"].n_unique()
#     b = df["subsector"].n_unique()
#     c = df["rfc_e"].n_unique()


#     df = (df.groupby(["mes"]).agg(
#         col("val_usd").sum(),
#         col("rfc_e").n_unique()
#         ))
    
#     d = format(int(df["val_usd"].sum() / 1000000), ',d')
#     f = format(int(df["val_usd"].mean()/ 1000000), ',d')
#     g = format(int(df["rfc_e"].mean()), ',d')
    
#     return [a, b, c, d, f, g, df]

# @st.cache_data()
# def get_list():
#     df = read_parquet("data/estados/lista_estados.parquet")
#     df = df.to_series().to_list()

#     return df

# @st.cache_data
# def get_states_data(state):
#     df = read_parquet("data/estados/" + state + ".parquet")

#     return df

# @st.cache_data
# def plot_map(state):
#     s = gpd.read_parquet("data/map_info/state_" + state + ".parquet")
#     map_info = gpd.read_parquet("data/map_info/cp_" + state + ".parquet")
    
#     return [s, map_info]


# estados = get_list()

# opcion = st.sidebar.selectbox(
#     "Selecciona estado",
#     estados
# )



# data = get_states_data(opcion)
# a, b, c, d, f, g, df_time = statistics(data)

# st.subheader(f"Informacion de {opcion}")
# col1, col2, col3 = st.columns(3)
# col1.markdown(metrics("Productos", a, "fas fa-globe-americas"), unsafe_allow_html=True)
# col2.markdown(metrics("Sectores", b, "fas fa-cogs"), unsafe_allow_html=True)
# col3.markdown(metrics("Empresas Totales", c, "fas fa-city"), unsafe_allow_html=True)

# col1, col2, col3 = st.columns(3)
# col1.markdown(metrics("Exportaciones totales", d + "M", "fas fa-globe-americas"), unsafe_allow_html=True)
# col2.markdown(metrics("Exportaciones promedio", f + " M", "fas fa-globe-americas"), unsafe_allow_html=True)
# col3.markdown(metrics("Empresas mensuales promedio", g, "fas fa-globe-americas"), unsafe_allow_html=True)


# st.header("Comportamiento Exportaciones")
# option = st.selectbox(
#     'Selecciona la variable',
#     ('Exportaciones', 'Numero_empresas'))
# s, map_info = plot_map(opcion)

# m = gen_maps(s, map_info)

# st_data = st_folium(m, width=500)

# def exp_section():
#     fig = gen_graphs(df_time, option)
#     df = gen_graphs(df_time, "tabla")
#     tab1, tab2 = st.tabs(["Gráfica", "Datos"])

#     with tab1:
#         # Plot!
#         st.plotly_chart(fig, use_container_width=True)
    
#     with tab2:
#         hide_table_row_index = """
#                     <style>
#                     thead tr th:first-child {display:none}
#                     tbody th {display:none}
#                     </>
#                     """
        
#         # Inject CSS with Markdown
#         st.markdown(hide_table_row_index, unsafe_allow_html=True)

#         # Table
#         st.table(df)

# exp_section()
# # st.subheader("10 productos mas vendidos")
# # st.dataframe(data)