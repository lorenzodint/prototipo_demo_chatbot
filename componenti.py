import streamlit as st
import time
from dotenv import load_dotenv
import os
import openai
from openai import OpenAI
from functions import *


def crea_sidebar():
    menuLaterale = st.sidebar
    with menuLaterale:
        if st.session_state.loggato == 0:
            # NAVIGAZIONE DA ESTERNO
            if st.button("Home"):
                st.session_state.page = 'home'
                #st.experimental_rerun()
                st.rerun()

            if st.button("Accedi"):
                st.session_state.page = 'login'
                #st.experimental_rerun()
                st.rerun()


            if st.button("Registrati"):
                st.session_state.page = 'register'
                #st.experimental_rerun()
                st.rerun()

        else:
            # NAVIGAZIONE DA ACCESSO
            if st.button("Nuova Chat"):
                st.session_state.chat = []
                st.session_state.titolo_chat = ""
                # st.experimental_rerun()
                st.rerun()

            st.divider()

            st.write("**Le tue Chat**:\n")

            lista()

            st.divider()



            col1, col2 = st.columns([1, 1])

            with col1:
                if st.button("Salva Chat"):
                    #pass
                    st.session_state.salva_chat = True
                    st.session_state.chat_input = False
                    #st.experimental_rerun()
                    st.rerun()

            with col2:
                if st.button("Svuota Chat"):
                    st.session_state.chat = []
                    st.session_state.titolo_chat = ""
                    #st.experimental_rerun()
                    st.rerun()

            col1, col2 = st.columns([1, 1])
            with col2:
                if st.button("Esci"):
                    st.session_state.page = "login"
                    st.session_state.loggato = False
                    st.session_state.chi_loggato = 0
                    st.session_state.chat = []
                    #st.experimental_rerun()
                    st.rerun()


def lista_chat():
    pass

def chat_bot():
    timestamp = time.time()

    if st.session_state.chat == []:
        primoMessaggio = gpt_start()
        st.session_state.chat.append(
            {
                "role": "assistant",
                "content": primoMessaggio,

            }
        )

    for messaggio in st.session_state.chat:
        if messaggio["role"] != "system":
            with st.chat_message(messaggio["role"]):
                st.markdown(messaggio['content'])

    # reagisci all'imput dell'utente
    if st.session_state.chat_input:
        if prompt := st.chat_input("Scrivi un messaggio"):
            # visualizza il messaggio dell'utente nella chat
            st.chat_message("user").markdown(prompt)
            # aggiungi il messaggio dell'utente all cronologia della chat
            timestamp = time.time()

            st.session_state.chat.append({
                "role": "user",
                "content": prompt,
                # "time": timestamp,
                # "titolo": ""
            })
            time.sleep(0.5)
            risposta = gpt_risposta()
            # risposta = "ahahaha"
            # visualizza risposta del bot nella chat
            with st.chat_message("assistant"):
                st.markdown(f"{risposta}")
            # aggiungi risposta alla cronologia della chat
            timestamp = time.time()
            st.session_state.chat.append({
                "role": "assistant",
                "content": risposta,
                # "time": timestamp,
                # "titolo": ""
            })


def salva_chat():
    st.warning("Inserisci un Titolo con cui salvare questa Chat")
    titolo = st.text_input("Crea un Titolo")

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Salva"):
            if not titolo:
                st.error("Inserire un titolo per la chat!")
            else:
                st.session_state.titolo_chat = titolo
                st.session_state.salvataggio = True
                st.rerun()

    with col2:
        if st.button("Annulla"):
            st.session_state.chat_input = True
            st.session_state.salva_chat = False
            st.session_state.salvataggio = False
            #st.experimental_rerun()
            st.rerun()


def test():
    st.title("consigliere libri")
    if "conversazione" not in st.session_state:
        st.session_state.conversazione = "Sei un chatbot consigliere di libri. Parliamo dei tuoi gusti per trovare il libro perfetto per te!\n"

    user_inp = st.text_input("Tu:", "")
    if user_inp:
        st.session_state.conversazione += f"Tu: {user_inp}\n"
        consiglio = "risposta chat gpt"
        st.session_state.conversazione += f"Consigliere: {consiglio}\n"
        # st.text_area("Conversazione", st.session_state.conversazione, height=300)

    st.text_area("Conversazione", st.session_state.conversazione, height=300)


def gpt_start():
    # Carica le variabili d'ambiente dal file .env
    load_dotenv()

    # Ottieni la chiave API da una variabile d'ambiente
    chiave_api = os.getenv("OPENAI_API_KEY")
    client = OpenAI(
        api_key=chiave_api
    )


    prompt_sistema = os.getenv("PROMPT_SISTEMA")

    sistema =prompt_sistema

    messaggio = {"role": "system", "content": sistema}

    st.session_state.chat.append(messaggio)

    risposta = client.chat.completions.create(
        messages=st.session_state.chat,
        model="gpt-3.5-turbo",
        n=1,
        # max_tokens=50,
        stop=None,
    )

    return risposta.choices[0].message.content


def gpt_risposta():
    # Carica le variabili d'ambiente dal file .env
    load_dotenv()

    # Ottieni la chiave API da una variabile d'ambiente
    chiave_api = os.getenv("OPENAI_API_KEY")
    client = OpenAI(
        api_key=chiave_api
    )

    risposta = client.chat.completions.create(
        messages=st.session_state.chat,
        model="gpt-3.5-turbo",
        n=1,
        # max_tokens=50,
        stop=None,
    )

    return risposta.choices[0].message.content




def lista():

    for ch in crea_lista_chat(st.session_state.chi_loggato):
        if st.button(ch[2]):
            st.session_state.chat = chat_text_obj(ch[3])



