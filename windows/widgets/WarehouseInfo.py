import kivy
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout

from windows.widgets.NumberPanelLabel import NumberPanelLabel
from windows.widgets.WarehouseInfoLabel import WarehouseInfoLabel

kivy.require('2.0.0')  # replace with your current kivy version !


# Panel wyświetlający ogólne informacje o stanie magazynu
class WarehouseInfoPanel(GridLayout):
    def __init__(self, **kwargs):
        super(WarehouseInfoPanel, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.cols = 2
        self.size_hint_y = 0.2

        # Utworzenie etkiet ze zmienną wartością tekstu
        self.occupation_label = Label(text="0%", size_hint_x=.3)
        self.exhaust_label = Label(text="0%", size_hint_x=.3)
        self.items_to_take_label = Label(text="0", size_hint_x=.3)
        self.items_to_spend_label = Label(text="0", size_hint_x=.3)
        self.is_crush_label = Label(text="NIE", size_hint_x=.3)
        self.is_break_label = Label(text="NIE", size_hint_x=.3)

        self.add_widget(WarehouseInfoLabel(text="Zapełnienie magazynu: "))
        self.add_widget(self.occupation_label)
        self.add_widget(WarehouseInfoLabel(text="Średnie zmęczenie pracownika: "))
        self.add_widget(self.exhaust_label)
        self.add_widget(WarehouseInfoLabel(text="Ilość towarów czekających na ułożenie na półkach: "))
        self.add_widget(self.items_to_take_label)
        self.add_widget(WarehouseInfoLabel(text="Ilość towarów czekających na wydanie: "))
        self.add_widget(self.items_to_spend_label)
        self.add_widget(WarehouseInfoLabel(text="Czy pracownicy mają przerwę: "))
        self.add_widget(self.is_break_label)
        self.add_widget(WarehouseInfoLabel(text="Czy występuje awaria: "))
        self.add_widget(self.is_crush_label)

    def refresh_warehouse_info(self, sim):
        self.occupation_label.text = "%s %%" % sim.get_warehouse_occupation()

        self.exhaust_label.text = "%s" % sim.get_employees_tiredness()
        self.items_to_take_label.text = "%s" % sim.get_deliveries_in_queue()
        self.items_to_spend_label.text = "%s" % sim.get_orders_in_queue()

        self.is_crush_label.text = "%s" % "TAK" if sim.get_is_crush() else "NIE"
        self.is_crush_label.color = (1, 0, 0, 1) if sim.get_is_crush() else (1, 1, 1, 1)

        self.is_break_label.text = "%s" % "TAK" if sim.get_is_break() else "NIE"
        self.is_break_label.color = (1, 1, 0, 1) if sim.get_is_break() else (1, 1, 1, 1)

