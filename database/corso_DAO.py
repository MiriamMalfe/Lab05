# Add whatever it is needed to interface with the DB Table corso

from database.DB_connect import get_connection
from model.corso import Corso


def getCorsi():
    corsi = []
    db = get_connection()
    cursor = db.cursor(dictionary=True)  # crea dizionario con info che trova su quella riga
    # -> per ogni riga del database mi crea una riga del dizionario

    cursor.execute("SELECT * FROM CORSO")
    for c in cursor:
        x = Corso(**c)  # prende tutto ciò che trova in c e lo mette dentro a
        # corsi senza che io debba specificare
        # attenzione all'ordine con cui metto gli attributi nella dataclass
        corsi.append(x)

    db.close()
    return corsi