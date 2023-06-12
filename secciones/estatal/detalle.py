import streamlit as st
from polars import col
from graphs.detalle import gen_table


def detalle_empresas(df, subsector):
    df1 = gen_table(df)
    df = gen_table(df)
    df = df[df["Subsector"] == subsector].reset_index(drop = True)

    st.dataframe(df)

    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv(index = False).encode('latin1')

    csv = convert_df(df)

    st.download_button(
        label="Descargar Tabla",
        data=csv,
        file_name='info_estados.csv',
        mime='text/csv',
    )