import streamlit as st


def session():
    if 'page' not in st.session_state:
        st.session_state.page = 'home'

    if 'loggato' not in st.session_state:
        st.session_state.loggato = 0

    if 'email_gia_registrata' not in st.session_state:
        st.session_state.email_gia_registrata = False

    if 'mostra_vai_login' not in st.session_state:
        st.session_state.mostra_vai_login = False

    if 'appena_registrato' not in st.session_state:
        st.session_state.appena_registrato = False

