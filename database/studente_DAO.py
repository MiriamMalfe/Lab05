# Add whatever it is needed to interface with the DB Table studente

from database.DB_connect import get_connection
from model.studente import Studente


def getStudente():
    studenti = {}

    db = get_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM STUDENTE")

    for s in cursor:
        x = Studente(**s)
        studenti[x.matricola] = x

    db.close()
    return studenti