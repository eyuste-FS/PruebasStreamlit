
import streamlit as st
from sqlite3 import Connection, Error


def addEntrada(entrada: str, publica: bool = False):

    username = st.session_state.get('username')
    if not username or not entrada:
        return False

    with Connection('appdata.sqlite') as conn:
        try:
            conn.execute(
                'insert into entradas (name, entrada, publica) '
                'values (?, ?, ?)',
                (username, entrada, publica))
            conn.commit()
        except Error:
            st.error('No se pudo añadir la entrada')
            return False
        else:
            st.success(entrada)
            st.toast('Entrada añadida')

    return True


def entrada_creation():
    st.subheader('Crear entrada')

    username = st.session_state.get('username')
    if not username:
        st.error('No se ha iniciado sesion')
        return

    with st.form('entrada_creation_form', True):

        entrada = st.text_input('Entrada')

        col1, _, col2 = st.columns(3)
        with col1:
            crear = st.form_submit_button('Crear')

        with col2:
            publica = st.checkbox('Hacer pública')

        if crear:
            return addEntrada(entrada, publica)

    return
