import plotly.express as px
from polars import col

def across_time(df, var):
    df = df.sort(col("mes"), descending = False)
    fig = px.line(x=df["mes"], y=df[var], 
              template="simple_white",
              color_discrete_sequence=["#9D2449"])
    fig.update_traces(mode="markers+lines", hovertemplate=None)
    # fig.update_layout(hovermode="x unified")

    fig.update_xaxes(
        title = "Mes",
        tickangle = 270,
        title_font = {"size": 14},
        color = "black"
        )
    fig.update_yaxes(
        title = var,
        title_font = {"size": 14},
        color = "black",
        )
    fig.update_layout(
        legend=dict(orientation='h', title = "", yanchor='bottom',xanchor='center',y=-0.5,x=0.5)
        )
    fig.update_layout(title_text="Exportaciones 240 productos en 2021", title_x=0.5, title_xanchor = "center")
    fig.update_traces(hovertemplate = '%{y:,.0f} ')
    
    return fig


def gen_table(df):
    df = df.to_pandas()
    df = df.rename(columns = {"mes": "Mes",
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

def gen_graphs(df, var):
    if var == "Exportaciones":
        fig = across_time(df, "val_usd")
        return fig
    if var == "Numero_empresas":
        fig = across_time(df, "rfc_e")
        return fig
    if var == "tabla":
        tab = table_style(df)
        return tab