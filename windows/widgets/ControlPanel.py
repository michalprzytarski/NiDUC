from windows.widgets.ControlGridPanel import ControlGridPanel

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import escape_markup
from kivy.uix.button import Button

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
        self.control_grid_panel = ControlGridPanel(sim)
        self.add_widget(self.control_grid_panel)

        # Przycisk start
        self.start_button = Button(text='START')
        self.start_button.size_hint_y = 0.1
        self.start_button.bind(on_press=lambda *args: self.start_callback(sim, sim_thread, *args))
        self.add_widget(self.start_button)

    # Metoda startująca symulacje
    def start_callback(self, sim, sim_thread, *arg):
        sim.init_environment(int(self.control_grid_panel.simulation_tempo_text_input.text))
        sim.init_warehouse(int(self.control_grid_panel.warehouse_space_text_input.text), int(self.control_grid_panel.number_of_start_items_text_input.text))
        sim.init_orders(int(self.control_grid_panel.number_of_daily_orders_text_input.text), 50)
        sim.init_delivery(int(self.control_grid_panel.number_of_daily_deliveries_text_input.text), 50)
        sim.set_employees_number(int(self.control_grid_panel.number_of_workers_text_input.text))
        sim.set_crush_probability(int(self.control_grid_panel.crush_probability_text_input.text))

        sim_thread.start()
        self.start_button.disabled = True
        self.control_grid_panel.add_orders_button.disabled = False
        self.control_grid_panel.add_delivery_button.disabled = False

        self.control_grid_panel.number_of_workers_text_input.disabled = True
        self.control_grid_panel.warehouse_space_text_input.disabled = True
        self.control_grid_panel.number_of_start_items_text_input.disabled = True
        self.control_grid_panel.number_of_daily_deliveries_text_input.disabled = True
        self.control_grid_panel.number_of_daily_orders_text_input.disabled = True
        self.control_grid_panel.crush_probability_text_input.disabled = True
        self.control_grid_panel.simulation_tempo_text_input.disabled = True

