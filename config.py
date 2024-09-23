import sqlite3


def connessione():# connessione db
    try:
        conn = sqlite3.connect("database.db")
        # print("connessione riuscita")
        result = [True, conn]
        return result
    except sqlite3.Error as error:
        result = [False, error]
        return result


def crea_tabella_utenti():
    if connessione()[0]:
        conn = connessione()[1]
        cursore = conn.cursor()

        query = ('CREATE TABLE IF NOT EXISTS `utenti` ('
                 '`id` INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL, '
                 '`email` VARCHAR(60) UNIQUE NOT NULL , '
                 '`pass` TEXT NOT NULL);')

        cursore.execute(query)

        conn.commit()
        conn.close()


def crea_teabella_chat():
    if connessione()[0]:
        conn = connessione()[1]
        cursore = conn.cursor()
        query = ('CREATE TABLE IF NOT EXISTS `chats`('
                 '`id` INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL, '
                 '`id_utente` VARCHAR(60) NOT NULL , '
                 '`titolo` VARCHAR(60) UNIQUE NOT NULL , '
                 '`chat` TEXT NOT NULL);')

        cursore.execute(query)

        conn.commit()
        conn.close()


