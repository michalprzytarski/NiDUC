import kivy
kivy.require('2.0.0') # replace with your current kivy version !

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.scrollview import ScrollView


class SimulationScreen(Widget):
    pass


class MainWindow(App):
    def build(self):
        self.title = 'Prototyp okna'
        return SimulationScreen()


if __name__ == '__main__':
    MainWindow().run()
