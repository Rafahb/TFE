import streamlit as st
import numpy as np
import pandas as pd
import functions

def getVariable(cabeceras, df):
    # Asignamos la primera columna con listado
    nombresList = df.iloc[:, 0].tolist()

    #Obtenemos los nombres seleccionados por el usuario
    nombresSelected = st.multiselect('Seleccionar '+cabeceras[0], options=nombresList)

    return nombresSelected

def getMetricas(cabeceras, df):
    #Creamos listado con las metricas
    listMetricas = []
    for i in cabeceras:
        if i != cabeceras[0]:
            listMetricas.append(i)

    #Obtenemos las metricas seleccionadas por el usuario
    metricasSelected = st.multiselect(
        'Seleccionar Metricas', options=listMetricas)

    return metricasSelected

def getDfEjemplo():
    df = pd.DataFrame()

    nombres = ['Lionel Messi', 'Cristiano Ronaldo', '...']
    metricas_a = ['20', '22', '...']
    metricas_b = ['15', '9', '...']
    metricas_c = ['24', '26', '...']

    df['Jugadores'] = nombres
    df['Gls'] = metricas_a
    df['Ass'] = metricas_b
    df['xG'] = metricas_c

    return df

if __name__ == "__main__":

    st.title("Radar Chart")

    #Solo permitido fichero csv y con formato primera columna nombre (jugador, equipo, liga) y resto de columnas metricas
    uploaded_file = st.file_uploader("Importar fichero csv")

    with st.beta_expander("Información"):
        st.write('''
        El formato permitido para importar el fichero es CSV. Y debe contener la siguiente estructura
        [VARIABLE (JUGADOR, EQUIPO o ENTRENADOR ...) + MÉTRICAS]
        ''')
        st.table(getDfEjemplo())

    if uploaded_file is not None:
        #Leemos fichero importado
        df = pd.read_csv(uploaded_file)

        # Mostramos tabla del fichero importado
        st.header("Fichero importado")
        st.write(df)

        # Cabeceras dataframe
        cabeceras = df.columns.values.tolist()

        # Obtenemos metricas seleccionados por el usuario
        nombresSelected = getVariable(cabeceras, df)

        if len(nombresSelected) != 2:
            st.error('Debe seleccionar solo dos ' +cabeceras[0])

        # Obtenemos nombres seleccionados por el usuario
        metricasSelected = getMetricas(cabeceras, df)

        if len(metricasSelected) < 3:
            st.error('Debe seleccionar al menos tres métricas')

        if (len(nombresSelected) == 2) & (len(metricasSelected) >= 3):
            #Creamos radar
            plt, df_final = functions.createRadar(df, metricasSelected,nombresSelected)
            st.pyplot(plt)
            st.table(df_final.reset_index(drop=True))

