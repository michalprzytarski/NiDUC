from windows.widgets.NumberPanelLabel import NumberPanelLabel
from windows.widgets.NumberPanelTextInput import NumberPanelTextInput

import kivy
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

kivy.require('2.0.0')  # replace with your current kivy version !


# Panel służący do wprowadzania wartości do InputText
class ControlGridPanel(GridLayout):
    def __init__(self, sim, **kwargs):
        super(ControlGridPanel, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.cols = 2
        self.spacing = (0, 30)

        # Wprowadzanie ilości pracowników
        self.add_widget(NumberPanelLabel(text='Ilość pracowników: '))
        self.number_of_workers_text_input = NumberPanelTextInput(text='20')
        self.add_widget(self.number_of_workers_text_input)

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

        # Przycisk Dodawania zamówień
        self.add_orders_button = Button(text='Dodaj 10 zamówień')
        self.add_orders_button.bind(on_press=sim.add_orders)
        self.add_orders_button.disabled = True
        self.add_widget(self.add_orders_button)

        # Przycisk dodawania dostaw
        self.add_delivery_button = Button(text='Dodaj 10 dostaw')
        self.add_delivery_button.bind(on_press=sim.add_deliveries)
        self.add_delivery_button.disabled = True
        self.add_widget(self.add_delivery_button)
