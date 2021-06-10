import simulation
import my_plot
import data_writer


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

        # # self.occupation_plot = my_plot.Plot()
        self.occupation_thread = Thread(target=my_plot.plot)
        # self.occupation_thread = Thread(target=my_plot.plot)
        self.occupation_thread.start()
        # my_plot.plot()
        # my_plot.plot(self, kill_thread=self.sim.kill_plot)
        self.occupation_writer = data_writer.DataWriter(filename='plots_data')

    # metoda wywoływana na ticku timera, używana do odświerzania okna
    def timer_tick(self, *args, **kwargs):
        if self.sim.war is not None:
            self.main_panel.info_panel.employee_list_scroll_view.employee_list_grid.refresh_employee_grid(self.sim.war.employees)
            self.main_panel.info_panel.warehouse_info_panel.refresh_warehouse_info(self.sim)

            self.occupation_writer.add_new_data(sim_time_to_add=self.sim.get_time(), occupation_to_add=self.sim.get_warehouse_occupation(), working_to_add=self.sim.get_current_working(), warehouse_empty_number_to_add=self.sim.get_warehouse_empty_number(), warehouse_idle_number_to_add=self.sim.get_warehouse_idle_number(), deliveries_number_to_add=self.sim.get_deliveries_in_queue(), orders_number_to_add=self.sim.get_orders_in_queue())
            if not self.sim_thread.is_alive():
                self.sim.war = None

    def build(self):
        self.title = 'Symulacja magazynu'

        # odświeżanie okna
        Clock.schedule_interval(self.timer_tick, 1.0/5.0)  # aplikacja okna 5 razy na sekunde wywoluje metode timer_tick

        return self.main_panel


if __name__ == '__main__':
    MainWindowApp().run()
