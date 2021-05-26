# import warehouse
import simulation
import threading
from threading import Thread
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock


kivy.require('2.0.0')  # replace with your current kivy version !


# Panel wypełniający całe okno
class MainPanel(BoxLayout):

    def __init__(self, sim, **kwargs):
        super(MainPanel, self).__init__(**kwargs)

        self.control_panel = ControlPanel(sim)
        self.add_widget(self.control_panel)

        self.info_panel = InfoPanel(sim)
        self.add_widget(self.info_panel)

    # def refresh(self, dt):
        # pass


# Panel służący do ustawiania parametrów symulacji
class ControlPanel(GridLayout):



    def __init__(self, sim, **kwargs):
        super(ControlPanel, self).__init__(**kwargs)

        self.sim = simulation.Simulation(100, 4, 1)
        self.sim_thread = Thread(target=sim.run)

        # Tytuł sekcji
        self.add_widget(Label(text="PARAMETRY SYMULACJI", text_size=(self.width, None)))

        # Panel zaweirający TextInput
        self.add_widget(NumberPanel())

        # Przycisk start
        self.start_button = Button(text='SATRT')
        self.start_button.bind(on_press=self.start_callback)                # DODAC METODE STARTUJACA
        self.add_widget(self.start_button)

        # Przycisk STOP
        self.stop_button = Button(text='STOP', disabled=True)
        self.stop_button.bind(on_press=self.stop_callback)                # DODAC METODE STOPUJACA
        self.add_widget(self.stop_button)

    def start_callback(self, *arg):
        # self.sim.test()
        self.sim_thread.start()
        self.start_button.disabled = True
        self.stop_button.disabled = False

        # sim.test()
        # sim.run()
        # print('The button <%s> is being pressed' % instance.text)

    def stop_callback(self, *arg):
        print('The button STOP is being pressed')
        # threading.currentThread().join()


# Panel służący do wprowadzania wartości do InputText
class NumberPanel(GridLayout):
    def __init__(self, **kwargs):
        super(NumberPanel, self).__init__(**kwargs)

        # Wprowadzanie ilości pracowników
        self.add_widget(NumberPanelLabel(text='Ilość pracowników: '))
        self.numberOfWorkersTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfWorkersTextInput)

        # Wprowadzanie ilości wózków widłowych
        self.add_widget(NumberPanelLabel(text='Ilość wózków widłowych: '))
        self.numberOfForkliftsTextInput = NumberPanelTextInput()
        self.add_widget(self.numberOfForkliftsTextInput)


# klasa używana do stylizowania Label w panelu ControlGridPanel
class NumberPanelLabel(Label):
    pass


# klasa uzywana do stylizowania TextInput w panelu ControlGridPanel
class NumberPanelTextInput(TextInput):
    pass


# panel wyświetlający informacje o aktualnym stanie symulacji
class InfoPanel(BoxLayout):
    def __init__(self, sim, **kwargs):
        super(InfoPanel, self).__init__(**kwargs)

        self.employee_list_scroll_view = EmployeeListScrollView(sim)
        self.add_widget(self.employee_list_scroll_view)

        self.warehouse_info_panel = WarehouseInfoPanel()
        self.add_widget(self.warehouse_info_panel)


# skrolowalna lista pracowników wraz z inforamacjami o nich
class EmployeeListScrollView(ScrollView):
    def __init__(self, sim, **kwargs):
        super(EmployeeListScrollView, self).__init__(**kwargs)

        self.employee_list_grid = EmployeeListGrid(sim)
        self.add_widget(self.employee_list_grid)


# panel znajdujący się w EmployeeListScrollView służący do porządkowania informacji o pracownikach
class EmployeeListGrid(GridLayout):
    def __init__(self, sim, **kwargs):
        super(EmployeeListGrid, self).__init__(**kwargs)

        for i in range(100):
            self.add_widget(EmployeeListLabel(text='Pracownik x'))
            self.add_widget(EmployeeListLabel(text='wolny'))
            self.add_widget(EmployeeListLabel(text='zmęczenie: 0'))

    def refresh_employee_grid(self):
        print("test odwierzania pracownikow")


# klasa uzywana do stylizowania informacji o pracowniku
class EmployeeListLabel(Label):
    pass


# Panel wyświetlający ogólne informacje o stanie magazynu
class WarehouseInfoPanel(GridLayout):
    def __init__(self, **kwargs):
        super(WarehouseInfoPanel, self).__init__(**kwargs)
        self.add_widget(Label(text="Zapełnienie magazynu: "))
        self.add_widget(Label(text="0%"))
        self.add_widget(Label(text="Średnie zmęczenie pracownika: "))
        self.add_widget(Label(text="0%"))
        self.add_widget(Label(text="Ilość oczekujących dostaw: "))
        self.add_widget(Label(text="0"))
        self.add_widget(Label(text="Ilość towarów czekających na ułożenie na półkach: "))
        self.add_widget(Label(text="0"))
        self.add_widget(Label(text="Ilość towarów czekających na wydanie: "))
        self.add_widget(Label(text="0"))


# Główne okno aplikacji
class MainWindow(App):

    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)
        self.sim = simulation.Simulation(100, 4, 1)

    # metoda wywoływana na ticku timera, używana do odświerzania okna
    def timer_tick(self, *args, **kwargs):
        pass
        # self.main_panel.info_panel.employee_list_scroll_view.employee_list_grid.refresh_employee_grid()
        # pass
        # print("test zegar")

    def build(self):
        self.title = 'Prototyp okna'

        # odświeżanie okna
        Clock.schedule_interval(self.timer_tick, 1.0)  #/60.0)  # aplikacja okna 60 razy na sekunde wywoluje metode timer_tick

        self.main_panel = MainPanel(self.sim)

        return self.main_panel


if __name__ == '__main__':
    MainWindow().run()
