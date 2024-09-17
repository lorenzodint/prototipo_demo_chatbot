import time
import re
import streamlit as st
from functions import controllo_email, aggiungi_utente
from componenti import crea_sidebar


def mostra_register():
    crea_sidebar()

    st.title("Registrazione")
    username = st.text_input("Inserisci la tua Email")
    password = st.text_input("Crea una Password", type="password")
    confirm_password = st.text_input("Conferma Password", type="password")

    # st.session_state.mostra_vai_login = False
    st.session_state.email_gia_registrata = False

    if st.button("Registrazione"):

        if username == "" or password == "" or confirm_password == "":
            st.error("I campi non possono essere vuoti!")

        elif len(password) < 8:
            st.error("La Password deve essere lunga almeno 8 caratteri!")
        elif re.search('[0-9]', password) is None:
            st.error("La Password deve contenere almeno un numero!")
        elif re.search('[A-Z]', password) is None:
            st.error("La Password deve contenere almeno un carattere maiuscolo!")
        elif re.search('[a-z]', password) is None:
            st.error("La Password deve contenere almeno un carattere minuscolo!")
        elif password != confirm_password:
            st.error("Le Password inserite non corrispondono!")

        else:
            controlloMail = controllo_email()
            # st.write(controlloMail)

            cont = 0
            for el in controlloMail:
                if username.lower() == el[1]:
                    cont = cont + 1
            if cont > 0:
                st.warning("Email già registrata, puoi effettuare l'accesso dalla pagina di Login!")
                st.session_state.email_gia_registrata = True

            else:
                st.warning("Registrazione in corso")
                st.session_state.email_gia_registrata = False
                st.session_state.mostra_vai_login = False
                aggiungi_utente(username, password)
                st.session_state.appena_registrato = True
                st.session_state.page = "login"
                time.sleep(1.5)
                # st.experimental_rerun()
                st.rerun()

    if "email_gia_registrata" in st.session_state and st.session_state.email_gia_registrata:
        # st.warning("utente gia registrato, effettuare login!")
        st.session_state.mostra_vai_login = True

    if st.session_state.mostra_vai_login:
        if st.button("Vai alla pagina di Login"):
            st.session_state.page = "login"
            st.session_state.email_gia_registrata = False
            st.session_state.mostra_vai_login = False
            # st.experimental_rerun()
            st.rerun()
