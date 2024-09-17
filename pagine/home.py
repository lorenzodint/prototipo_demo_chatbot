import streamlit as st
from componenti import crea_sidebar

def mostra_home():

    crea_sidebar()



    # Titolo principale
    st.title("Benvenuto su <*piattaforma*>")

    #st.write("""## Il ChatBot che trova il libro adatto a te""")

    # Descrizione del progetto
    st.write("""
    ### Scopri il tuo prossimo libro preferito!

    Sei stanco di passare ore alla ricerca del libro perfetto? Il nostro chatbot è qui per aiutarti! In base ai tuoi gusti e preferenze, il nostro chatbot intelligente ti consiglierà i libri che adorerai. Basta avere una conversazione con il nostro bot e capirà i tuoi gusti e le tue antipatie per fornirti consigli personalizzati.
    """)


    # Sezione sui benefici del progetto
    st.markdown("""
    ## Perchè usare il nostro ChatBot?

    - **Consigli personalizzati**:  ricevi suggerimenti di libri personalizzati in base alle tue preferenze.
    - **Facile da usare**:  chatta con il nostro bot e lascia che faccia il resto.
    - **Risparmia tempo**:  trova rapidamente i libri che corrispondono ai tuoi interessi senza ricerche infinite.

    ## Come Funziona?

    1. **Chatta con il bot**: avvia una conversazione con il nostro chatbot.
    2. **Esprimi le tue preferenze**:  parla dei tuoi generi, dei tuoi autori preferiti e di ciò che cerchi in un libro.
    3. **Ricevi consigli**:  ricevi un elenco di libri che corrispondono alle tue preferenze.

    ## Inizia ad usarlo ora!

    Fai clic sul pulsante in basso per iniziare la conversazione con il nostro chatbot per consigliare libri.
    """)


    if st.button("Inizia Ora"):
        st.session_state.page = "login"
        #st.experimental_rerun()
        st.rerun()







