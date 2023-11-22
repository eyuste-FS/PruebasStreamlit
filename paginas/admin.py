
import streamlit as st


def admin():

    if st.session_state.get('username') != st.secrets.get('admin_username'):
        st.error('No tienes permiso para ver esta pagina')
        return

    st.markdown('''
    ## Pagina de administracion
    Estas registrado como {}.
    '''.format(st.session_state.get('username')))

    return
