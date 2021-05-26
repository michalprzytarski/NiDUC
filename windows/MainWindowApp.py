import simulation
from windows.widgets.MainPanel import MainPanel

import kivy
from kivy.app import App
from kivy.clock import Clock

kivy.require('2.0.0')  # replace with your current kivy version !

# Główne okno aplikacji
class main_window(App):

    def __init__(self, **kwargs):
        super(main_window, self).__init__(**kwargs)
        self.sim = simulation.Simulation(100, 20, 1)
        self.main_panel = MainPanel(self.sim)

    # metoda wywoływana na ticku timera, używana do odświerzania okna
    def timer_tick(self, *args, **kwargs):
        self.main_panel.info_panel.employee_list_scroll_view.employee_list_grid.refresh_employee_grid(self.sim.war.employees)

    def build(self):
        self.title = 'Symulacja magazynu'

        # odświeżanie okna
        Clock.schedule_interval(self.timer_tick, 1.0/60.0)  # aplikacja okna 60 razy na sekunde wywoluje metode timer_tick

        return self.main_panel


if __name__ == '__main__':
    main_window().run()