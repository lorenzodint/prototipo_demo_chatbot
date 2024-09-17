import streamlit as st
from componenti import crea_sidebar, chat_bot, salva_chat



def mostra_dashboard():
    if not st.session_state.salva_chat:
        crea_sidebar()
    st.title("DASHBOARD")


    if st.session_state.salva_chat:
        st.session_state.chat_input = False
        salva_chat()



    chat_bot()



