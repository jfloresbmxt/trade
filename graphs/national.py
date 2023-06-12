import plotly.express as px
from polars import read_parquet, col

def treemap(df, n):
    colors = ["#13322B", "#285C4D",
          "#B38E5D", "#D4C19C", 
          "#56242A", "#9D2449"]
    
    df = df.to_pandas()

    fig = px.treemap(df.head(n), path=["Título", "desc_partida", "descripcion"], values = "val_usd",
                    color = "Título",
                    #  hover_data=[1],
                    color_discrete_sequence = colors
                    #  width=900, height=900
                    )

    fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

    template = '''
    <b>Subsector / descripcción de producto:</b> %{label} <br>
    <b>Total exportaciones:</b> %{value} 
    '''
    fig.update_traces(hovertemplate=template)

    return fig

def gen_table(df):
    df = df.to_pandas()
    df = df.rename(columns = {
        "Título": "Subsector",
        "desc_partida": "Partida",
        "descripcion": "Descripcion producto",
        "val_usd": "Exportaciones"})

    return df

def table_style(df):
    df = gen_table(df)
    # style
    th_props = [
    ('font-size', '16px'),
    ('text-align', 'center'),
    ('font-weight', 'bold'),
    ('color', '#ffffff'),
    ('background-color', '#B38E5D')
    ]

    td_props = [
    ('font-size', '14px')
    ]

    styles = [
    dict(selector="th", props=th_props),
    dict(selector="td", props=td_props)
    ]

    # table
    df = (df.style
        .format(precision=0, thousands=",")
        .set_properties(**{'text-align': 'left'})
        .set_table_styles(styles))
    
    return df


def gen_treemap(df, n, option):
    if option == "grafica":
        return treemap(df, n)
    if option == "tabla":
        return table_style(df)