import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout


kivy.require('2.0.0')  # replace with your current kivy version !


# Panel wypełniający całe okno
class MainPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(MainPanel, self).__init__(**kwargs)

        control_panel = ControlPanel()
        self.add_widget(control_panel)

        info_panel = InfoPanel()
        self.add_widget(info_panel)


# Panel służący do ustawiania parametrów symulacji
class ControlPanel(GridLayout):
    def __init__(self, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)

        # Tytuł sekcji
        self.add_widget(Label(text="PARAMETRY SYMULACJI", text_size=(self.width, None)))

        # Panel zaweirający TextInput
        self.add_widget(NumberPanel())

        # Przycisk start
        self.start_button = Button(text='SATRT')
        # self.start_button.bind(on_press=)                #DODAC METODE STARTUJACA
        self.add_widget(self.start_button)

        # Przycisk STOP
        self.stopButton = Button(text='STOP')
        # self.stopButton.bind(on_press=)                #DODAC METODE STARTUJACA
        self.add_widget(self.stopButton)


# Panel służący do wprowadzania wartości do InputText
class NumberPanel(GridLayout):
    def __init__(self, **kwargs):
        super(NumberPanel, self).__init__(**kwargs)

        # Wprowadzanie ilości pracowników
        self.add_widget(NumberPanelLabel(text='Ilość pracowników: '))
        self.numberOfWorkersTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfWorkersTextInput)

        # Wprowadzanie ilości wózków widłowych
        self.add_widget(NumberPanelLabel(text='Ilość wózków widłowych: '))
        self.numberOfForkliftsTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfForkliftsTextInput)


# klasa używana do stylizowania Label w panelu NumberPanel
class NumberPanelLabel(Label):
    pass


# klasa uzywana do stylizowania TextInput w panelu NumberPanel
class NumberPanelTextInput(TextInput):
    pass


# panel wyświetlający informacje o aktualnym stanie symulacji
class InfoPanel(BoxLayout):
    def __init__(self, **kwargs):
        super(InfoPanel, self).__init__(**kwargs)

        employee_list_scroll_view = EmployeeListScrollView()
        self.add_widget(employee_list_scroll_view)

        warehouse_info_panel = WarehouseInfoPanel()
        self.add_widget(warehouse_info_panel)


# skrolowalna lista pracowników wraz z inforamacjami o nich
class EmployeeListScrollView(ScrollView):
    def __init__(self, **kwargs):
        super(EmployeeListScrollView, self).__init__(**kwargs)

        employee_list_grid = EmployeeListGrid()
        self.add_widget(employee_list_grid)


# panel znajdujący się w EmployeeListScrollView służący do porządkowania informacji o pracownikach
class EmployeeListGrid(GridLayout):
    def __init__(self, **kwargs):
        super(EmployeeListGrid, self).__init__(**kwargs)
        self.add_widget(EmployeeListLabel(text='Pracownik x'))
        self.add_widget(EmployeeListLabel(text='wolny'))
        self.add_widget(EmployeeListLabel(text='zmęczenie: 0'))


# klasa uzywana do stylizowania informacji o pracowniku
class EmployeeListLabel(Label):
    pass


# Panel wyświetlający ogólne informacje o stanie magazynu
class WarehouseInfoPanel(GridLayout):
    def __init__(self, **kwargs):
        super(WarehouseInfoPanel, self).__init__(**kwargs)
        self.add_widget(Label(text="Zapełnienie magazynu: "))
        self.add_widget(Label(text="0%"))
        self.add_widget(Label(text="Średnie zmęczenie pracownika: "))
        self.add_widget(Label(text="0%"))
        self.add_widget(Label(text="Ilość oczekujących dostaw: "))
        self.add_widget(Label(text="0"))
        self.add_widget(Label(text="Ilość towarów czekających na ułożenie na półkach: "))
        self.add_widget(Label(text="0"))
        self.add_widget(Label(text="Ilość towarów czekających na wydanie: "))
        self.add_widget(Label(text="0"))


# Główne okno aplikacji
class MainWindow(App):
    def build(self):
        self.title = 'Symulacja magazynu'
        main_panel = MainPanel()
        return main_panel


if __name__ == '__main__':
    MainWindow().run()
