import flet as ft
from database.corso_DAO import getCorsi
from database.iscrizione_DAO import getIscrizioni, setIscrizione
from database.studente_DAO import getStudente


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self.corsi = []
        self.studenti = {}

    def cercaIscritti(self, e):
        c = self._view.ddCorsi.value
        if c is None:
            self._view.create_alert("Seleziona un corso")
            self._view.update_page()
            return

        self.studenti = getStudente()
        iscrizioni = getIscrizioni()

        for q in iscrizioni:
            if q[0] == c:
                stringa = "nome: " + self.studenti[q[1]].nome + ", " + "cognome: " + self.studenti[q[1]].cognome + ", matricola: " + str(self.studenti[q[1]].matricola)  # per accedee al dizionario
                self._view.lv.controls.append(ft.Text(stringa))
                self._view.update_page()

    def cercaStudente(self, e):
        m = self._view.matricola.value()
        if m is None:
            self._view.create_alert("Inserire una matricola")
            self._view.update_page()
            return
        elif m.isdigit():
            self.studenti = getStudente()

            if self.studenti.__contains__(int(m)):
                nome = self.studenti[int(m)].nome
                cognome = self.studenti[int(m)].cognome
                self._view.nome.value = nome
                self._view.cognome.value = cognome
                self._view.update_page()
            else:
                self._view.create_alert("La matricola inserita non esiste")
                self._view.update_page()
                return


    def cercaCorsi(self, e):
        m = self._view.matricola.value()
        if m is None:
            self._view.create_alert("Inserire una matricola")
            self._view.update_page()
            return
        elif m.isdigit():
            iscrizioni = getIscrizioni()
            trovato = 0

            for c in iscrizioni:
                if c[1] == int(m):
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

            self.studenti = getIscrizioni()

            if self.studenti.__contains__(int(m)):
                iscrizioni = getIscrizioni()
                for cu in iscrizioni:
                    if cu[0] == cod and cu[1] == int(m):
                        self._view.create_alert("Studente già iscritto a questo corso")
                        self._view.update_page()
                        return
                query = "INSERT INTO 'iscrizione' ('matricola', 'codins') VALUES ("+str(m)+", '"+cod+"')"
                dati = (m, cod)
                setIscrizione(query, dati)

    def fillCorsi(self):

        corsi = getCorsi()

        for c in corsi:
            self._view.ddCorsi.options.append(ft.dropdown.Option(key=c.codins, text=c.nome))
