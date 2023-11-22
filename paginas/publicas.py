
import streamlit as st
from sqlite3 import Connection, Error
from math import ceil
from typing import List, Tuple

PAGESIZE = 3


@st.cache_data(ttl=20)
def getEntradasPublicas(page: int = None) -> List[Tuple[str, str]]:

    if not st.session_state.get('username'):
        st.error('Debes iniciar sesion para cargar las entradas publicas')
        return []

    consulta = (
        'select name, entrada from entradas where publica order by id desc', ()
        ) if page is None else (
        'select name, entrada from entradas where '
        'publica order by id desc limit ?, ?', (page * PAGESIZE, PAGESIZE))

    with Connection('appdata.sqlite') as conn:
        try:
            res = conn.execute(*consulta).fetchall()
        except Error:
            st.error('Ocurrió un error al acceder a la base de datos')
            return []

    return res


@st.cache_data(ttl=20)
def getNEntradasPublicas() -> int:

    with Connection('appdata.sqlite') as conn:
        try:
            res = conn.execute(
                'select count(*) from entradas where publica').fetchone()
        except Error:
            st.error('Ocurrió un error al acceder a la base de datos')
            return -1

    if not len(res):
        return -1

    return res[0]


@st.cache_data(ttl=18)
def entradasToBars():

    d = dict()
    for nombre, _ in getEntradasPublicas():
        d[nombre] = d.get(nombre, 0) + 1

    return d


def publicas():

    username = st.session_state.get('username')
    if not username:
        return

    maxpageidx = ceil(getNEntradasPublicas() / PAGESIZE) - 1
    page = st.session_state.get('publicpageidx')
    if page is None:
        st.session_state['publicpageidx'] = page = 0

    elif page < 0 or page > maxpageidx:
        st.session_state['publicpageidx'] = page = min(
            max(0, page), maxpageidx)

    with st.expander('Entradas públicas', True):

        for nombre, entrada in getEntradasPublicas(page):
            if nombre == username:
                st.markdown(f'''_**({nombre})**_ : {entrada}''')
            else:
                st.markdown(f'''_**{nombre}**_ : {entrada}''')

    col1, col2, col3 = st.columns(3)
    with col1:
        prev = st.button('<', key='pagprev', disabled=(page <= 0))

    with col2:
        st.write(f'Página {page + 1} / {maxpageidx + 1}')

    with col3:
        nex = st.button(
            '\\>', key='pagnext', disabled=(page >= maxpageidx))

    if prev:
        st.session_state['publicpageidx'] -= 1
        st.rerun()
    if nex:
        st.session_state['publicpageidx'] += 1
        st.rerun()

    st.subheader('Entradas públicas por usuario')
    datad = entradasToBars()
    st.bar_chart(datad)
