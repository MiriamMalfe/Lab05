import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Lab O5 - segreteria studenti"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None
        # graphical elements
        self._title = None
        self.txt_name = None
        self.ddCorsi=None
        self.cercaIscritti=None
        self.matricola =None
        self.nome =None
        self.cognome =None
        self.cercaStudente =None
        self.cercaCorsi =None
        self.iscriviti =None
        self.lv=None


    def load_interface(self):
        """Function that loads the graphical elements of the view"""
        # title
        self._title = ft.Text("App Gestione studenti", color="blue", size=24)
        row1 = ft.Row([self._title], alignment=ft.MainAxisAlignment.CENTER)

        self.ddCorsi = ft.Dropdown(label="Corso", hint_text="Seleziona un corso", width=600)
        self.cercaIscritti=ft.ElevatedButton(text="Cerca iscritti", on_click=self._controller.cercaIscritti)
        row2 = ft.Row([self.ddCorsi, self.cercaIscritti], alignment=ft.MainAxisAlignment.CENTER)

        self.matricola=ft.TextField(label="Matricola", width=200, hint_text="Inserisci la matricola")
        self.nome= ft.TextField(label="Nome", width=200, read_only=True)
        self.cognome= ft.TextField(label="Cognome", width=200, read_only=True)
        row3 = ft.Row([self.matricola, self.nome, self.cognome], alignment= ft.MainAxisAlignment.CENTER)

        self.cercaStudente = ft.ElevatedButton(text="Cerca studente", on_click=self._controller.cercaStudente)
        self.cercaCorsi= ft.ElevatedButton(text="Cerca corsi", on_click=self._controller.cercaCorsi)
        self.iscriviti= ft.ElevatedButton(text="Iscriviti", on_click=self._controller.iscriviti)
        row4=ft.Row([self.cercaStudente, self.cercaCorsi, self.iscriviti], alignment= ft.MainAxisAlignment.CENTER)

        self.lv=ft.ListView(expand=True)
        row5= ft.Row([self.lv], alignment=ft.MainAxisAlignment.CENTER)

        self._controller.fillCorsi()
        self._page.add(row1, row2, row3, row4, row5)

    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        """Function that opens a popup alert window, displaying a message
        :param message: the message to be displayed"""
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()


