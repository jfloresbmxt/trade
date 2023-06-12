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