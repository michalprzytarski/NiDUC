import kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

kivy.require('2.0.0')  # replace with your current kivy version !


# Panel wyświetlający ogólne informacje o stanie magazynu
class WarehouseInfoPanel(GridLayout):
    def __init__(self, **kwargs):
        super(WarehouseInfoPanel, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.cols = 2
        self.size_hint_y = 0.2

        # Utworzenie etkiet ze zmienną wartością tekstu
        self.occupation_label = Label(text="0%", size_hint_x=.1)
        self.exhaust_label = Label(text="0%", size_hint_x=.1)
        self.delivery_label = Label(text="0", size_hint_x=.1)
        self.items_to_take = Label(text="0", size_hint_x=.1)
        self.items_to_spend = Label(text="0", size_hint_x=.1)

        self.add_widget(Label(text="Zapełnienie magazynu: "))
        self.add_widget(self.occupation_label)
        self.add_widget(Label(text="Średnie zmęczenie pracownika: "))
        self.add_widget(self.exhaust_label)
        self.add_widget(Label(text="Ilość oczekujących dostaw: "))
        self.add_widget(self.delivery_label)
        self.add_widget(Label(text="Ilość towarów czekających na ułożenie na półkach: "))
        self.add_widget(self.items_to_take)
        self.add_widget(Label(text="Ilość towarów czekających na wydanie: "))
        self.add_widget(self.items_to_spend)

    def refresh_warehouse_info(self, war):
        self.occupation_label.text = "%s" % war.capacity
        tiredness = 0
        for employee in war.employees:
            tiredness += employee.tiredness
        if len(war.employees) != 0:
            tiredness = tiredness // len(war.employees)
        self.exhaust_label.text = "%s" % tiredness
        self.delivery_label.text = "test"
        self.items_to_take.text = "test"
        self.items_to_spend.text = "test"

