import geopandas as gpd
import contextily as cx

def gen_maps(s,map_info):
    m = s.explore(name="Polygons",
                    tiles = cx.providers.CartoDB.Positron,
                    style_kwds=dict(fillColor="white",color="gray", fillOpacity=1),
                    )
    m = map_info.explore(m=m,
                    column="Numero de empresas",
                    tooltip="Municipio",
                    popup= ["Codigo postal", "Municipio", "Numero de empresas", "Exportaciones"],
                    cmap="Reds",
                    style_kwds=dict(color="black", fillOpacity = 1),
                    map_kwds = dict(zoom_control = False),
                    name="Points")
    return m

def plot_map(state):
    s = gpd.read_parquet("data/map_info/state_" + state + ".parquet")
    map_info = gpd.read_parquet("data/map_info/cp_" + state + ".parquet")
    m = gen_maps(s, map_info)

    return m