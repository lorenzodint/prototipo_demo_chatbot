import sqlite3
import hashlib
from openai import OpenAI
import os
from dotenv import load_dotenv
import streamlit as st
from config import connessione

def aggiungi_utente(email, password):
    try:

        if connessione()[0]:
            conn = connessione()[1]
            cursore = conn.cursor()
            pass_hash = hashlib.sha256(password.encode()).hexdigest()
            query = (' INSERT INTO utenti '
                     '(email, pass) '
                     'VALUES (?, ?)')

            cursore.execute(query, (email, pass_hash))

            conn.commit()
            conn.close()
    except:
        print("errore query aggiungi utente")


def elimina_utente(email):
    try:

        if connessione()[0]:
            conn = connessione()[1]
            cursore = conn.cursor()
            query = (' DELETE FROM utenti WHERE email = ?')

            cursore.execute(query, (email,))

            conn.commit()
            conn.close()
    except:
        print("errore query elimina utente")


def elimina_tab(tabella):
    try:

        if connessione()[0]:
            conn = connessione()[1]
            cursore = conn.cursor()
            query = (' DROP TABLE {}')

            cursore.execute(query.format(tabella))

            conn.commit()
            conn.close()
    except:
        print("errore query elimina tabella")


# elimina_utente("silvestro@gmail.com")
# aggiungi_utente("sara@gmail.com", "Password1234")
# elimina_tab("chats")

def controllo_email():
    if connessione()[0]:
        conn = connessione()[1]
        cursore = conn.cursor()
        query = 'SELECT * FROM utenti'
        cursore.execute(query)
        risultato = cursore.fetchall()
        conn.close()
        return risultato


def controllo_credenziali(email, password):
    if connessione()[0]:
        conn = connessione()[1]
        cursore = conn.cursor()
        pass_hash = hashlib.sha256(password.encode()).hexdigest()
        user = email.lower()
        query = ' SELECT * FROM utenti WHERE email = ? AND pass = ?'
        cursore.execute(query, (user, pass_hash))
        utente = cursore.fetchone()
        conn.close()
        return utente


'''def gpt_start(prompt):
    # Configura l'API di OpenAI
    openai.api_key = 'sk-proj-q3wZ86uMMEkFX530zlGST3BlbkFJoBrKBfsDCPNMnKf6LA5i'
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()'''


def gpt(input_utente):
    # Carica le variabili d'ambiente dal file .env
    load_dotenv()

    # Ottieni la chiave API da una variabile d'ambiente
    chiave_api = os.getenv("OPENAI_API_KEY")

    client = OpenAI(
        api_key=chiave_api,
    )

    response = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": input_utente
            }
        ],
        model="gpt-3.5-turbo",
        n=1,
        max_tokens=50,
        stop=None,
    )

    return response.choices[0].message.content


def chat_obj_text():
    testo = ""
    for messaggio in st.session_state.chat:
        testo += "@$?"
        if messaggio["role"] == "system":
            testo += "$SY="
            testo += messaggio["content"]

        elif messaggio["role"] == "assistant":
            testo += "$AS="
            testo += messaggio["content"]

        elif messaggio["role"] == "user":
            testo += "$US="
            testo += messaggio["content"]

    return testo

def chat_text_obj(testo):
    chat = []
    elem = testo.split("@$?")
    for item in elem:
        if item == "":
            elem.remove(item)
    for item in elem:
        if item[:4] == "$SY=":
            chat.append({
                "role": "system",
                "content": item[4:]
            })
        if item[:4] == "$AS=":
            chat.append({
                "role": "assistant",
                "content": item[4:]
            })

        if item[:4] == "$US=":
            chat.append({
                "role": "user",
                "content": item[4:]
            })

    return chat



def select_all(tabella):
    if connessione()[0]:
        conn = connessione()[1]
        cursore = conn.cursor()
        query = 'SELECT * FROM {}'
        cursore.execute(query.format(tabella))
        risultato = cursore.fetchall()
        conn.close()
        return risultato


def select_1(tabella, colonna1, parametro1):
    if connessione()[0]:
        conn = connessione()[1]
        cursore = conn.cursor()
        query = 'SELECT * FROM {} WHERE {} = {}'
        cursore.execute(query.format(tabella, colonna1, parametro1))
        risultato = cursore.fetchall()
        conn.close()
        return risultato


def salva_chat_db(testo):
    try:

        if select_all("chats") == []:
            if connessione()[0]:
                conn = connessione()[1]
                cursore = conn.cursor()
                query = (' INSERT INTO chats '
                         '(id_utente, titolo, chat) '
                         'VALUES (?, ?, ?)')

                cursore.execute(query, (st.session_state.chi_loggato, st.session_state.titolo_chat, testo))

                conn.commit()
                conn.close()
        else:
            for riga in select_all("chats"):
                if riga[2] == st.session_state.titolo_chat:
                    aggiorna_chat_db(testo)
                    return None
            if connessione()[0]:
                conn = connessione()[1]
                cursore = conn.cursor()
                query = (' INSERT INTO chats '
                         '(id_utente, titolo, chat) '
                         'VALUES (?, ?, ?)')

                cursore.execute(query, (st.session_state.chi_loggato, st.session_state.titolo_chat, testo))

                conn.commit()
                conn.close()


    except sqlite3.Error as er:
        print("errore query salva chat")
        print("\n\n")
        print(er)


def aggiorna_chat_db(testo):
    try:
        if connessione()[0]:
            conn = connessione()[1]
            cursore = conn.cursor()
            query = ('UPDATE chats '
                     'SET '
                     'chat = {},'
                     'WHERE '
                     'titolo = {}')

            cursore.execute(query.format(testo, st.session_state.titolo_chat))

            conn.commit()
            conn.close()

    except:
        print("errore query aggiorna chat")
        print("\n\n")


def crea_lista_chat(utente):
    try:
        if connessione()[0]:
            conn = connessione()[1]
            cursore = conn.cursor()
            query = ('SELECT * FROM chats '
                     'WHERE id_utente = {}')
            cursore.execute(query.format(utente))
            risultato = cursore.fetchall()
            #conn.commit()
            conn.close()
            return risultato

    except sqlite3.Error as er:
        print("Errore crea_lista_chat")
