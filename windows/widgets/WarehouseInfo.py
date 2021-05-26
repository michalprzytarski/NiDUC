import kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

kivy.require('2.0.0')  # replace with your current kivy version !

# Panel wyświetlający ogólne informacje o stanie magazynu
class WarehouseInfoPanel(GridLayout):
    def __init__(self, **kwargs):
        super(WarehouseInfoPanel, self).__init__(**kwargs)

        self.cols = 2
        self.size_hint_y = 0.2

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