import dbm.sqlite3

from database.DB_connect import get_connection

def getIscrizioni():

    iscrizioni = []
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ISCRIZIONE")

    for c in cursor:
        iscrizioni.append((c["codins"], c["matricola"]))

    db.close()
    return iscrizioni

def setIscrizione(query1, query2):
    db = get_connection()
    cursor = db.cursor()

    cursor.execute(query1, query2)

    db.close()