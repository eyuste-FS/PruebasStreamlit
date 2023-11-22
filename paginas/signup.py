

import streamlit as st
from sqlite3 import Connection, Error


def try_signup(user: str, pwd: str) -> bool:

    # Insertar en db
    inserted = False
    with Connection('appdata.sqlite') as conn:
        try:
            conn.execute(
                '''insert into usuarios (name, password) values (?, ?)''',
                (user, pwd))
            conn.commit()
        except Error:
            ...
        else:
            inserted = True

    # Verificar insercion
    if not inserted:
        st.error('Ocurrió un error al crear el usuario')
        return False

    st.session_state['username'] = user
    del st.session_state['currentpage']
    return True


def password_check(pwd: str) -> bool:

    if not pwd:
        st.error('Introduce una contraseña')
        return False

    if len(pwd) < 4:
        st.error('La contraseña debe tener al menos 4 caracteres')
        return False

    return True


def username_check(username: str) -> bool:

    if not username:
        return False

    with Connection('appdata.sqlite') as conn:
        existent = conn.execute('''
            select name from usuarios where name = ?
            ''', (username, )).fetchone()

    print('SIGNUP >', existent)
    if existent:
        st.error('Ya existe el usuario {}'.format(username))
        return False

    return True


def signup():

    username = st.session_state.get('username')
    if username:
        st.error((
            'Ya has iniciado sesión como "{}", cierra sesión para crear '
            'un nuevo usuario').format(username))
        return

    st.markdown('''
    ## Signup
    Crear nueva cuenta
    ''')

    with st.form('signup_form'):

        user = st.text_input('Usuario')
        pwd = st.text_input('Contraseña', type='password')

        submit = st.form_submit_button('Aceptar')
        if submit:
            if not username_check(user):
                return False
            if not password_check(pwd):
                return False
            return try_signup(user, pwd)

    return
