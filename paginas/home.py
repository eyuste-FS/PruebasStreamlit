
import streamlit as st
from sqlite3 import Connection
from .publicas import publicas


def getSecrets():
    username = st.session_state.get('username')
    if not username:
        return []

    with Connection('appdata.sqlite') as conn:
        res = conn.execute('''
        select entrada from entradas where name = ? order by id desc
        ''', (username, )).fetchall()

    return [row[0] for row in res]


def home():

    st.subheader('Página de inicio')

    entradas = getSecrets()
    if entradas:
        with st.expander('Entradas propias'):
            for entrada in entradas:
                st.code(entrada)

    publicas()
