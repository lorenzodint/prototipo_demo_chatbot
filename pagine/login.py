import streamlit as st
from componenti import crea_sidebar
from functions import controllo_credenziali


def mostra_login():
    crea_sidebar()

    if st.session_state.appena_registrato:
        st.warning("Accedi con le credenziali appena registrate")

    st.title("Accedi")
    username = st.text_input("Email")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([1, 1])

    with col1:
        pulsante_accedi = st.button("Accesso")
        if pulsante_accedi:
            if username == "" or password == "":
                st.error("I campi non possono essere vuoti!")
            else:
                utente = controllo_credenziali(username, password)
                if utente == None:
                    #st.write("non presente")
                    st.error("Email o password errati")
                else:
                    #st.write("presente")
                    #st.write(utente)
                    log = utente[0]
                    st.session_state.loggato = True
                    st.session_state.chi_loggato = int(log)
                    st.session_state.page = "dashboard"
                    #st.experimental_rerun()
                    st.rerun()

    with col2:
        if st.button("Password dimenticata?"):
            st.write("non ricordo la password...")




    #st.warning("test GPT")
    #st.write(gpt_start())