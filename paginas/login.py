'''
Version de pruebas

Contraseñas en texto plano:
Sin hashes/salts/etc
'''


import streamlit as st
from sqlite3 import Connection


def wrong_login(msg):
    st.toast(msg)


def try_login(username, password):
    if not username:
        wrong_login('El campo Usuario es obligatorio')
        return False

    if not password:
        wrong_login('El campo Contraseña es obligatorio')
        return False

    with Connection('appdata.sqlite') as conn:
        res = conn.execute('''
            select name, password from usuarios where name = ? and password = ?
            ''', (username, password)).fetchone()

    if not res or len(res) != 2 or res[0] != username or res[1] != password:
        wrong_login('Error en el par usuario/contraseña')
        return False

    st.session_state['username'] = res[0]

    return True


def login():

    username = st.session_state.get('username')
    if username is not None:
        st.success(f'Ya has iniciado sesion como {username}')
        return

    st.markdown('''
    ## Login
    Debes iniciar sesión para continuar
    ''')

    with st.form('login_form', False):

        user = st.text_input('Usuario')
        pwd = st.text_input('Contraseña', type='password')

        col1, _, col2 = st.columns(3)
        with col1:
            submit = st.form_submit_button('Iniciar sesión')

        with col2:
            signup = st.form_submit_button('Crear nueva cuenta')

        if submit:
            return try_login(user, pwd)
        if signup:
            st.session_state['currentpage'] = 'signup'
            st.rerun()
            return

    return
