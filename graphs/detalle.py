from polars import read_parquet

def gen_table(df):
    df = df.to_pandas()
    df["Título"] = df["Título"].apply(lambda x: x.replace("T", ""))
    df["Título"] = df["Título"].apply(lambda x: x.strip())
    
    for i in ["razon_social_e", "colonia_e", "calle_e"]:
        df[i] = df[i].apply(lambda x: x.capitalize())
    
    df["val_usd"] = df["val_usd"]/1000
    df = df.rename(columns = {"razon_social_e": "Razon Social",
                              "Título": "Subsector",
                              "d_estado": "Estado",
                              "D_mnpio": "Municipio",
                              "colonia_e": "Colonia",
                              "calle_e": "Calle",
                              "num_ext": "Numero exterior",
                              "val_usd": "Exportaciones (Miles de dolares)"
                              })
    df = df[["Razon Social", "Subsector", "Estado", "Municipio", "Colonia", "Calle", "Numero exterior", "Exportaciones (Miles de dolares)"]]

    return df

def table_style(df):
    # df = gen_table(df)
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