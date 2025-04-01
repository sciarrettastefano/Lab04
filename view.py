import flet as ft

class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self.__controller = None
        # UI elements
        self.__title = None
        self.__theme_switch = None

        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self.__title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self.__theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        self.page.controls.append(
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title, ],
                   alignment=ft.MainAxisAlignment.START)
        )

        # Add your stuff here

        # Riga 1: menù per scegliere la lingua
        self._ddLanguage = ft.Dropdown(
            label = "Language",
            width = 750
        )
        self._ddLanguage.options.append(ft.dropdown.Option("Italian"))
        self._ddLanguage.options.append(ft.dropdown.Option("English"))
        self._ddLanguage.options.append(ft.dropdown.Option("Spanish"))
        row1 = ft.Row([self._ddLanguage], ft.MainAxisAlignment.START)

        # Riga 2: manù per scegliere modalità di ricerca + spazio per inserire il proprio testo + bottone per avviare il controllo
        self._ddModality = ft.Dropdown(
            label = "Search Modality",
            width = 200
        )
        self._ddModality.options.append(ft.dropdown.Option("Default"))
        self._ddModality.options.append(ft.dropdown.Option("Linear"))
        self._ddModality.options.append(ft.dropdown.Option("Dichotomic"))
        self._txtIn = ft.TextField(
            label = "Add your sentence here",
            width = 430
        )
        self._btnSpellCheck = ft.ElevatedButton(
            text="Spell Check",
            on_click = self.__controller.handleSentence
        )
        row2 = ft.Row([self._ddModality, self._txtIn, self._btnSpellCheck], ft.MainAxisAlignment.START)

        # In più: aggiungo un bottone che fa pulire la ListView quando vuole l'utente
        self._btnClear = ft.ElevatedButton(
            text="Clear",
            on_click = self.__controller.handleClear,
            width = 300
        )
        row3 = ft.Row([self._btnClear], ft.MainAxisAlignment.CENTER)

        # ListView per avere riscontro
        self._txtOut = ft.ListView(expand = True)

        self.page.add(row1, row2, row3, self._txtOut)

    def update(self):
        self.page.update()

    def setController(self, controller):
        self.__controller = controller

    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self.__theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
