import plotly.express as px

def bar_sectors_exp(df):
    df = df.sort("val_usd", descending = True)

    fig = px.bar(df, x = df['subsector'], y = df["val_usd"],
             title = "Exportaciones por subsector", 
             template = 'plotly_white',
             hover_name = df['Título'],
             custom_data= [0],
             color_discrete_sequence = ["#D4C19C"]
             )

    fig.update_layout(
        title = {
            'text': "Exportaciones por sector 2021",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        xaxis = {
            'title':"Código del subsector"
            },
        yaxis = {
            'title':"Exportaciones"
            },
        hoverlabel = {
            'bgcolor': "white",
            'font_size': 16,
            'font_family': "Rockwell"
            }
        )
    fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br> <br> Número de empresas: <b>%{y}</b>')

    return fig

def bar_sectors_n(df):
    df = df.sort("rfc_e", descending = True)

    fig = px.bar(df, x = df['subsector'], y = df["rfc_e"],
             title = "Exportaciones por subsector", 
             template = 'plotly_white',
             hover_name = df['Título'],
             custom_data= [0],
             color_discrete_sequence = ["#D4C19C"]
             )

    fig.update_layout(
        title = {
            'text': "Número de empresas que exportan por sector 2021",
            'y': 0.9,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top'
            },
        xaxis = {
            'title':"Código del subsector"
            },
        yaxis = {
            'title':"Número de empresas"
            },
        hoverlabel = {
            'bgcolor': "white",
            'font_size': 16,
            'font_family': "Rockwell"
            }
        )
    fig.update_traces(hovertemplate='<b>%{customdata[0]}</b> <br> <br> Número de empresas: <b>%{y}</b>')

    return fig

def gen_table(df):
    df = df.to_pandas()
    df["Subsector"] = df["subsector"].str.cat(df["Título"], sep = "-")
    df["Subsector"] = df["Subsector"].apply(lambda x: x.replace("T", ""))
    # df = df.drop(columns={"Título", "subsector"})
    df = df.rename(columns = {"rfc_e": "Empresas",
                              "val_usd": "Exportaciones"})
    df = df[["Subsector", "Exportaciones", "Empresas"]]

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

def gen_sectors_graphs(df, var):
    if var == "Exportaciones":
        fig = bar_sectors_exp(df)
        return fig
    if var == "Numero_empresas":
        fig = bar_sectors_n(df)
        return fig
    if var == "tabla":
        tab =  table_style(df)
        return tab