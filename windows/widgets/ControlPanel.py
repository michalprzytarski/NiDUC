from windows.widgets.ControlGridPanel import ControlGridPanel

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import escape_markup

kivy.require('2.0.0')  # replace with your current kivy version !


# Panel służący do ustawiania parametrów symulacji
class ControlPanel(BoxLayout):
    def __init__(self, sim, sim_thread, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)

        self.orientation = 'vertical'

        # Dodanie styli do obiektu
        self.size_hint_x = 0.33
        self.padding = 10

        # Tytuł sekcji
        text = 'PARAMETRY SYMULACJI'
        parameters_label = Label(text='[b]' + '[u]' + '[size=24]' + escape_markup(text) + '[/size]' + '[/u]' + '[/b]', markup=True)
        parameters_label.size_hint_y = None
        self.add_widget(parameters_label)

        # Panel zaweirający 2 kolumny z polami do wprowadzania wartości
        self.add_widget(ControlGridPanel(sim, sim_thread))


