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
        self.spacing = (0, 10)

        # Wprowadzanie ilości pracowników
        self.add_widget(NumberPanelLabel(text='Ilość pracowników: '))
        self.numberOfWorkersTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfWorkersTextInput)

        # Wprowadzanie ilości wózków widłowych
        self.add_widget(NumberPanelLabel(text='Ilość wózków widłowych: '))
        self.numberOfForkliftsTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfForkliftsTextInput)

        # Wprowadzanie powierzchni magazynowej
        self.add_widget(NumberPanelLabel(text='Powierzchnia magazynowa: '))
        self.warehouse_space = NumberPanelTextInput()
        self.add_widget(self.warehouse_space)

        # Wprowadzanie ilości dostaw dziennie
        self.add_widget(NumberPanelLabel(text='Ilość dostaw dziennie: '))
        self.number_of_daily_deliveries = NumberPanelTextInput()
        self.add_widget(self.number_of_daily_deliveries)

        # Przycisk start
        self.start_button = Button(text='START')
        self.start_button
        self.start_button.size = (self.width * 0.5, self.height * 0.5)
        self.start_button.bind(on_press=lambda *args: self.start_callback(sim_thread, *args))
        self.add_widget(self.start_button)

        # Przycisk STOP
        self.stop_button = Button(text='STOP', disabled=True, padding=(10, 10))
        self.stop_button.bind(on_press=self.stop_callback)
        self.add_widget(self.stop_button)

    # Metoda startująca symulacje
    def start_callback(self, sim_thread, *arg):
        sim_thread.start()
        self.start_button.disabled = True
        self.stop_button.disabled = False

    # Metoda stopująca symulacje
    def stop_callback(self, *arg):
        print('The button STOP is being pressed')
        # threading.currentThread().join()