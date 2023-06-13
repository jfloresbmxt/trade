#functions
import contextily as cx


def gen_mapa_mun(map_info):
    m = map_info.explore(
        column = "Exportaciones",
        tiles = cx.providers.CartoDB.Positron,
        style_kwds=dict(color="gray", fillOpacity=1),
        cmap = "Reds"
        )
    
    return m