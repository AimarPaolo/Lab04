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
            ft.Row(spacing=30, controls=[self.__theme_switch, self.__title],
                   alignment=ft.MainAxisAlignment.START)
        )
        # Add your stuff here
        self._selectLanguage = ft.Dropdown(label="Select language", width=600, on_change=self.__controller.handleChange1)
        self.fillWords(1)
        row2 = ft.Row([self._selectLanguage])
        self._searchModality = ft.Dropdown(label="Search Modality ", width=200, on_change=self.__controller.handleChange2)
        self._txtIn = ft.TextField(label="Add your sentence here", width=200)
        self._btnCheck = ft.ElevatedButton(text="Spell Check", on_click=self.__controller.handleSpellCheck)
        self.fillWords(2)
        row3 = ft.Row([self._searchModality, self._txtIn, self._btnCheck])
        self._lvOut = ft.ListView()
        row4 = ft.Row([self._lvOut])
        self.page.add(row2, row3, row4)
        self.page.update()

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

    def fillWords(self, numero):
        if numero == 1:
            self._selectLanguage.options.append(ft.dropdown.Option("english"))
            self._selectLanguage.options.append(ft.dropdown.Option("italian"))
            self._selectLanguage.options.append(ft.dropdown.Option("spanish"))

        if numero == 2:
            self._searchModality.options.append(ft.dropdown.Option("Linear"))
            self._searchModality.options.append(ft.dropdown.Option("Default"))
            self._searchModality.options.append(ft.dropdown.Option("Dichotomic"))

