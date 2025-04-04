import flet as ft
from database.DB_connect import get_connection
from model.corso import Corso
from model.studente import Studente


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corsi = []
        self.studenti = {}

    def cercaIscritti(self, e):
        p = self._view.ddCorsi.value
        if p is None:
            self._view.create_alert("Seleziona un corso")
            self._view.update_page()
            return
        db = get_connection()
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM STUDENTE")
        for c in cursor:
            s = Studente(**c)
            self.studenti[s.matricola] = s

        cursor.execute("SELECT * FROM ISCRIZIONE")
        for cu in cursor:
            if cu["codins"] == p:
                stringa=""
                stringa = "nome: "+self.studenti[cu["matricola"]].nome+", "+"cognome: "+self.studenti[cu["matricola"]].cognome+", matricola: "+str(self.studenti[cu["matricola"]].matricola) #per accedee al dizionario
                self._view.lv.controls.append(ft.Text(stringa))
                self._view.update_page()
        db.close()

    def cercaStudente(self, e):
        m = self._view.matricola.value()
        if m is None:
            self._view.create_alert("Inserire una matricola")
            self._view.update_page()
            return
        elif m.isdigit():
            db = get_connection()
            cursor = db.cursor(dictionary = True)
            cursor.execute("SELECT * FROM STUDENTE")
            self.studenti.clear()  #mi svuota ciò che c'era prima delntro a quel dizionario
            for c in cursor:
                s = Studente(**c)
                self.studenti[s.matricola] = s
                db.close()
            if self.studenti.__contains__(int(m)):
                self._view.nome.value(self.studenti[int(m)].nome)
                self._view.cognome.value(self.studenti[int(m)].cognome)
                self._view.update_page()
            else:
                self._view.create_alert("La matricola inserita non esiste")


    def cercaCorsi(self, e):
        m = self._view.matricola.value()
        if m is None:
            self._view.create_alert("Inserire una matricola")
            self._view.update_page()
            return
        elif m.isdigit():
            db = get_connection()
            cursor = db.cursor(dictionary = True)
            cursor.execute("SELECT * FROM ISCRIZIONE")
            self.studenti.clear()
            trovato = 0
            for c in cursor:
                if c["matricola"] == int(m):
                    stringa = ""
                    stringa = "Codice corso: "+c["codins"]
                    self._view.lv.controls.append(ft.Text(stringa))
                    self._view.update_page()
                    trovato = 1
            if trovato == 0:
                self._view.create_alert("Matricola non trovata")
                self._view.update_page()


    def iscriviti(self, e):
        m = self._view.matricola.value
        cod = self._view.ddCorsi.value
        if m is None:
            self._view.create_alert("Inserire una matricola")
            self._view.update_page()
            return
        elif m.isdigit():
            if cod is None:
                self._view.create_alert("Seleziona un corso")
                self._view.update_page()
                return
            db = get_connection()
            cursor = db.cursor(dictionary=True)
            cursor.execute("SELECT * FROM STUDENTE")
            self.studenti.clear()
            for c in cursor:
                s = Studente(**c)
                self.studenti[s.matricola] = s
            if self.studenti.__contains__(int(m)):
                cursor.execute("SELECT * FROM ISCRIZIONE")
                for cu in cursor:
                    if cu["codins"] == cod and cu["matricola"] == int(m):
                        self._view.create_alert("Studente già iscritto a questo corso")
                        self._view.update_page()
                        return
                query = "INSERT INTO 'iscrizione' ('matricola', 'codins') VALUES ("+str(m)+", '"+cod+"')"
                cursor.execute(query)



    def fillCorsi(self):
        db=get_connection()
        cursor=db.cursor(dictionary=True)  #crea dizionario con info che trova su quella riga
                                            # -> per ogni riga del database mi crea una riga del dizionario

        cursor.execute("SELECT * FROM CORSO")
        for c in cursor:
            x = Corso(**c)   #prende tutto ciò che trova in c e lo mette dentro a
                                # corsi senza che io debba specificare
                            #attenzione all'ordine con cui metto gli attributi nella dataclass
            self.corsi.append(x)
            self._view.ddCorsi.options.append(ft.dropdown.Option(key=x.codins, text=x.nome))

        db.close()