import time

from pagine import home, login, register, dashboard
from config import crea_tabella_utenti, crea_teabella_chat
from functions import *

# creazione tabella utenti su database
crea_tabella_utenti()
# creazione tabella chat su database
crea_teabella_chat()

# inizializzazione stato della sessione per la pagina
# sessionState.session()

if 'page' not in st.session_state: # pagina di navigazione
    st.session_state.page = 'home'

if 'loggato' not in st.session_state: # utente loggato
    st.session_state.loggato = False

if 'chi_loggato' not in st.session_state: # chi è loggato
    st.session_state.chi_loggato = 0

if 'email_gia_registrata' not in st.session_state: # email già registrata (fase di registrazione)
    st.session_state.email_gia_registrata = False

if 'mostra_vai_login' not in st.session_state: # indirizzamento pagina di login
    st.session_state.mostra_vai_login = False

if 'appena_registrato' not in st.session_state: # utente appena registrato
    st.session_state.appena_registrato = False

if 'chat' not in st.session_state: # chat
    st.session_state.chat = []

if 'chat_input' not in st.session_state: # mostra/nascondi input chat
    st.session_state.chat_input = True

if 'salva_chat' not in st.session_state: # salva chat
    st.session_state.salva_chat = False

if 'titolo_chat' not in st.session_state: # titolo chat
    st.session_state.titolo_chat = ""

if 'salvataggio' not in st.session_state: # fase di salvataggio
    st.session_state.salvataggio = False

# st.session_state.pop("click_vai_login", None)



# errore fase login, reset sessioni -> pagina login
if st.session_state.loggato == False and st.session_state.chi_loggato != 0:
    st.session_state.page = "login"
    st.session_state.loggato = False
    st.session_state.chi_loggato = 0
    st.error("Errore Login")
    time.sleep(1.5)
    # st.experimental_rerun()
    st.rerun()


# fase di salvataaggio -> conversione chat + salvataggio
if st.session_state.salvataggio:
    testo = chat_obj_text()
    salva_chat_db(testo)

    st.session_state.chat_input = True
    st.session_state.salvataggio = False
    st.session_state.salva_chat = False
    # st.experimental_rerun()
    st.rerun()

# Mostra la pagina corrente
if st.session_state.page == 'home':
    home.mostra_home()
    st.session_state.mostra_vai_login = False
    st.session_state.email_gia_registrata = False
    st.session_state.appena_registrato = False
elif st.session_state.page == 'login':
    login.mostra_login()
    st.session_state.mostra_vai_login = False
    st.session_state.email_gia_registrata = False
    st.session_state.appena_registrato = False

elif st.session_state.page == 'register':
    register.mostra_register()
    st.session_state.appena_registrato = False

elif st.session_state.page == "dashboard":
    dashboard.mostra_dashboard()
    st.session_state.appena_registrato = False


#st.write(st.session_state)


#st.write(st.session_state.chat)

#st.write(crea_lista_chat(st.session_state.chi_loggato))

# st.write(chat_obj_text())
