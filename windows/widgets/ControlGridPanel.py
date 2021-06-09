from windows.widgets.NumberPanelLabel import NumberPanelLabel
from windows.widgets.NumberPanelTextInput import NumberPanelTextInput

import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

kivy.require('2.0.0')  # replace with your current kivy version !

# Panel służący do wprowadzania wartości do InputText
class ControlGridPanel(GridLayout):
    def __init__(self, sim, sim_thread, **kwargs):
        super(ControlGridPanel, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.cols = 2
        self.spacing = (0, 30)

        # Wprowadzanie ilości pracowników
        self.add_widget(NumberPanelLabel(text='Ilość pracowników: '))
        self.number_of_workers_text_input = NumberPanelTextInput(text='20')
        self.add_widget(self.number_of_workers_text_input)

        # # Wprowadzanie ilości wózków widłowych
        # self.add_widget(NumberPanelLabel(text='Ilość wózków widłowych: '))
        # self.number_of_forklifts_text_input = NumberPanelTextInput(text='5')
        # self.add_widget(self.number_of_forklifts_text_input)

        # Wprowadzanie powierzchni magazynowej
        self.add_widget(NumberPanelLabel(text='Powierzchnia magazynowa: '))
        self.warehouse_space_text_input = NumberPanelTextInput(text='100')
        self.add_widget(self.warehouse_space_text_input)

        # Wprowadzanie ilości towarów na start symulacji
        self.add_widget(NumberPanelLabel(text='Ilość towarów startowych: '))
        self.number_of_start_items_text_input = NumberPanelTextInput(text='10')
        self.add_widget(self.number_of_start_items_text_input)

        # Wprowadzanie tempa przychodzenia dostaw
        self.add_widget(NumberPanelLabel(text='Tempo przychodzenia dostaw: '))
        self.number_of_daily_deliveries_text_input = NumberPanelTextInput(text='2')
        self.add_widget(self.number_of_daily_deliveries_text_input)

        # Wprowadzanie tempa przychodzenia zamówień
        self.add_widget(NumberPanelLabel(text='Tempo przychodzenia zamówień: '))
        self.number_of_daily_orders_text_input = NumberPanelTextInput(text='2')
        self.add_widget(self.number_of_daily_orders_text_input)

        # Wprowadzanie prawdopodobieństwa awarii
        self.add_widget(NumberPanelLabel(text='Prawdopodobieństwo awarii: '))
        self.crush_probability_text_input = NumberPanelTextInput(text='1')
        self.add_widget(self.crush_probability_text_input)

        # Wprowadzanie tempa symulacji
        self.add_widget(NumberPanelLabel(text='Tempo symulacji: '))
        self.simulation_tempo_text_input = NumberPanelTextInput(text='1')
        self.add_widget(self.simulation_tempo_text_input)

        # Przycisk start
        self.start_button = Button(text='START')
        self.start_button.bind(on_press=lambda *args: self.start_callback(sim, sim_thread, *args))
        self.add_widget(self.start_button)

        # Przycisk STOP
        self.stop_button = Button(text='STOP', padding=(10, 10))
        self.stop_button.bind(on_press=self.stop_callback)
        self.add_widget(self.stop_button)

        # Przycisk Dodawania zamówień
        self.add_orders_button = Button(text='Dodaj 10 zamówień')
        self.add_orders_button.bind(on_press=sim.add_orders)
        self.add_orders_button.disabled = True
        self.add_widget(self.add_orders_button)

        # Przycisk dodawania dostaw
        self.add_delivery_button = Button(text='Dodaj 10 dostaw')
        self.add_delivery_button.bind()
        self.add_delivery_button.disabled = True
        self.add_widget(self.add_delivery_button)

    # Metoda startująca symulacje
    def start_callback(self, sim, sim_thread, *arg):
        sim.init_environment(int(self.simulation_tempo_text_input.text))
        sim.init_warehouse(int(self.warehouse_space_text_input.text), int(self.number_of_start_items_text_input.text))
        sim.init_orders(int(self.number_of_daily_orders_text_input.text), 50)
        sim.init_delivery(int(self.number_of_daily_deliveries_text_input.text), 50)
        sim.set_employees_number(int(self.number_of_workers_text_input.text))
        sim.set_crush_probability(int(self.crush_probability_text_input.text))

        sim_thread.start()
        self.start_button.disabled = True
        # self.stop_button.disabled = False
        self.add_orders_button.disabled = False
        self.add_delivery_button.disabled = False

        self.number_of_workers_text_input.disabled = True
        # self.number_of_forklifts_text_input.disabled = True
        self.warehouse_space_text_input.disabled = True
        self.number_of_start_items_text_input.disabled = True
        self.number_of_daily_deliveries_text_input.disabled = True
        self.number_of_daily_orders_text_input.disabled = True
        self.crush_probability_text_input.disabled = True
        self.simulation_tempo_text_input.disabled = True

    # Metoda stopująca symulacje
    def stop_callback(self):
        # sim.setKillPlot(True)
        print('The button STOP is being pressed')
        # threading.currentThread().join()