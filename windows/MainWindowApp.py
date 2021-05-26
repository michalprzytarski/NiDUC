import simulation
from windows.widgets.MainPanel import MainPanel

from threading import Thread

import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.core.window import Window

kivy.require('2.0.0')  # replace with your current kivy version !

# Dołączenie pliku styli kivy
Builder.load_file("kv.kv")

# Zmiana wielkości okna
Window.size = (1280, 720)

# Zmiana startowej pozycji okna
Window.top = 100
Window.left = 50


# Główne okno aplikacji
class MainWindowApp(App):

    def __init__(self, **kwargs):
        super(MainWindowApp, self).__init__(**kwargs)
        self.sim = simulation.Simulation()
        self.sim_thread = Thread(target=self.sim.run)
        self.main_panel = MainPanel(self.sim, self.sim_thread)

    # metoda wywoływana na ticku timera, używana do odświerzania okna
    def timer_tick(self, *args, **kwargs):
        if self.sim.war != None:
            self.main_panel.info_panel.employee_list_scroll_view.employee_list_grid.refresh_employee_grid(self.sim.war.employees)
            self.main_panel.info_panel.warehouse_info_panel.refresh_warehouse_info(self.sim)

    def build(self):
        self.title = 'Symulacja magazynu'

        # odświeżanie okna
        Clock.schedule_interval(self.timer_tick, 1.0/60.0)  # aplikacja okna 60 razy na sekunde wywoluje metode timer_tick

        return self.main_panel


if __name__ == '__main__':
    MainWindowApp().run()