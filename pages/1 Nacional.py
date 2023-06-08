import streamlit as st
from css.metrics import metrics
from polars import read_parquet, col
from graphs.across_time import gen_graphs
from graphs.sector import gen_sectors_graphs
from graphs.states import gen_states_graphs


@st.cache_data
def get_national_data():
    df = read_parquet('data/statistics.parquet')
    a = df.select(col("Productos")).rows(named=True)[0]["Productos"]
    b = df.select(col("Subsectores")).rows(named=True)[0]["Subsectores"]
    c = df.select(col("Empresas")).rows(named=True)[0]["Empresas"]

    df_time = read_parquet("data/across_time.parquet")
    emp_prom = int((df_time["rfc_e"].mean()))
    sum_exp = int(df_time["val_usd"].sum()/100000)
    exp_prom = int(df_time["val_usd"].mean()/100000)

    df_sectors = read_parquet("data/sectors.parquet")
    df_states = read_parquet("data/estados.parquet")

    return [a,b,c, df_time, df_sectors, 
            df_states, emp_prom, sum_exp, exp_prom]

a,b,c, df_time, df_sectors, df_states, emp_prom, sum_exp, exp_prom = get_national_data()

# Title
st.title("Información Nacional")

# Description
st.markdown("En esta sección podras encontrar información nacional de 240 productos")

col1, col2, col3 = st.columns(3)
col1.markdown(metrics("Productos", a, "fas fa-globe-americas"), unsafe_allow_html=True)
col2.markdown(metrics("Sectores", b, "fas fa-cogs"), unsafe_allow_html=True)
col3.markdown(metrics("Empresas Totales", format(c, ',d'), "fas fa-city"), unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
col1.markdown(metrics("Exportaciones totales", format(sum_exp, ',d'), "fas fa-globe-americas"), unsafe_allow_html=True)
col2.markdown(metrics("Exportaciones promedio", format(exp_prom, ',d') + " M", "fas fa-globe-americas"), unsafe_allow_html=True)
col3.markdown(metrics("Empresas mensuales promedio", format(emp_prom, ',d'), "fas fa-globe-americas"), unsafe_allow_html=True)


st.header("Comportamiento Exportaciones")
option = st.selectbox(
    'Selecciona la variable',
    ('Exportaciones', 'Numero_empresas'))

def exp_section():
    fig = gen_graphs(df_time, option)
    df = gen_graphs(df_time, "tabla")
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

def sectors_section(option):
    fig = gen_sectors_graphs(df_sectors, option)
    table = gen_sectors_graphs(df_sectors, "tabla")
    tab1, tab2 = st.tabs(["Gráfica", "Datos"])

    with tab1:
        # Plot!
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
        
        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # Table
        st.table(table)


st.header("Informacion sectorial")
sectors_section(option)

def states_section(option):
    fig = gen_states_graphs(df_states, option)
    table = gen_states_graphs(df_states, "tabla")
    tab1, tab2 = st.tabs(["Gráfica", "Datos"])

    with tab1:
        # Plot!
        st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        hide_table_row_index = """
                    <style>
                    thead tr th:first-child {display:none}
                    tbody th {display:none}
                    </style>
                    """
        
        # Inject CSS with Markdown
        st.markdown(hide_table_row_index, unsafe_allow_html=True)

        # Table
        st.table(table)

st.header("Informacion estatal")
states_section(option)
