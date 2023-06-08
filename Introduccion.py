import streamlit as st

st.set_page_config(
    page_title="240 productos",
    page_icon="airplane",
)

# Esconder Menu por default
# hide_menu()

st.title('Oportunidades nearshoring')

st.header("Objetivo")
st.markdown('''Con el objetivo de identificar los productos donde México tiene una mayor 
            probabilidad de aumentar sus exportaciones hacia EUA de forma inmediata y sustituir 
            proveeduría asiática se realizó un ejercicio que considera tres factores: 
            * Mercado objetivo en EUA, productos donde EUA demanda más de 50 millones
            de dólares (musd) anuales desde Asia;  
            * capacidad exportadora de México, bienes donde México ya vende a EUA más de 50 mdd anuales; 
            * sustituibilidad inmediata, bienes intermedios que pueden ser intercambiables entre proveedores.''')
st.subheader("Contexto Macroeconomico")
st.markdown('''El contexto macroeconómico global está generando una reconfiguración de la 
            producción mundial. Algunos factores de la coyuntura son: conflicto comercial 
            EUA – China, regionalización productiva e interrupción de las cadenas de suministro, 
            entre otros.''')
st.divider()