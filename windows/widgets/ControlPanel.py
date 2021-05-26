import simulation
from threading import Thread

from windows.widgets.NumberPanel import NumberPanel

import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

kivy.require('2.0.0')  # replace with your current kivy version !

# Panel służący do ustawiania parametrów symulacji
class ControlPanel(GridLayout):
    def __init__(self, sim, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)

        # Dodanie styli do obiektu
        self.cols = 1
        self.size_hint_x = 0.33

        # Inicjalizacja zmiennych używanych w klasie
        self.sim = simulation.Simulation(100, 4, 1)
        self.sim_thread = Thread(target=sim.run)

        # Tytuł sekcji
        self.add_widget(Label(text="PARAMETRY SYMULACJI", text_size=(self.width, None)))

        # Panel zaweirający TextInput
        self.add_widget(NumberPanel())

        # Przycisk start
        self.start_button = Button(text='SATRT')
        self.start_button.size = (self.width*0.5, self.height*0.5)
        self.start_button.bind(on_press=self.start_callback)
        self.add_widget(self.start_button)

        # Przycisk STOP
        self.stop_button = Button(text='STOP', disabled=True)
        self.stop_button.bind(on_press=self.stop_callback)
        self.add_widget(self.stop_button)

        # Metoda startująca symulacje
    def start_callback(self, *arg):
        self.sim_thread.start()
        self.start_button.disabled = True
        self.stop_button.disabled = False

        # Metoda stopująca symulacje
    def stop_callback(self, *arg):
        print('The button STOP is being pressed')
        # threading.currentThread().join()
