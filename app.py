
import streamlit as st
from paginas.login import login
from paginas.home import home
from paginas.creacion import entrada_creation
from paginas.admin import admin
from paginas.signup import signup
from os.path import exists

if not exists('appdata.sqlite'):  # TEMP
    import createdb  # noqa: F401

print('Session State Debug', st.session_state)  # TEMP (debug)


# Definicion de las paginas
paginas = [
    # (nombre, key),
    ('Home', 'home', home),
    ('Crear entrada', 'create', entrada_creation)
]

st.title('App')

# Login/Signup
username = st.session_state.get('username')
if username is None:
    if st.session_state.get('currentpage') == 'signup':
        if signup():
            st.rerun()
    elif login():
        st.rerun()
    st.stop()


if username == st.secrets.get('admin_username'):
    paginas.append(('Administracion', 'admin', admin))


# Sidebar

with st.sidebar:

    st.markdown('Has iniciado sesion como **{}**'.format(username))
    col_out, col_empty, col_reload = st.columns(3)
    # Logout
    with col_out:
        if st.button('Logout'):
            if 'username' in st.session_state:
                del st.session_state['username']
                st.rerun()
    with col_reload:
        if st.button('Reload'):
            st.rerun()

    st.divider()
    st.title('Páginas accesibles')

    # seleccion
    for i, (titulo, key, _) in enumerate(paginas):

        if st.button(titulo, key=f'{titulo}_{i}'):
            st.session_state['currentpage'] = key

# Contenido principal

page = st.session_state.get('currentpage')
if page is None:
    home()
    st.stop()

for _, key, func in paginas:
    if page == key:
        func()
        break

else:
    if 'currentpage' in st.session_state:
        del st.session_state['currentpage']
    st.rerun()
