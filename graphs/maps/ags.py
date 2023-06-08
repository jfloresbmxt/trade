import geopandas as gpd
import contextily as cx

def gen_data(df):
    shp_file = gpd.read_file("data/shapefiles/CP_01Ags_v9.shp")

    df = df.to_pandas()
    df_cp = df.groupby("cp_e").agg({"val_usd": "sum"}).reset_index()

    map_ = shp_file.merge(df_cp, how = "inner", left_on = "d_codigo", right_on= "cp_e")
    map_["val_usd"] = map_["val_usd"].fillna(0)
    
    return [shp_file, map_]

def gen_map(shapefile, datamap):
    m = shapefile.explore(name="Polygons",
                     tiles = cx.providers.CartoDB.Positron,
                     popup=True,
                     style_kwds=dict(color="black", fillOpacity=0.1))
    
    m = datamap.explore(m=m,
                 column="val_usd",
                 style_kwds=dict(fillOpacity=1),
                 name="Points")
    return m