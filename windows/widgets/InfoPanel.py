from windows.widgets.EmployeeListScrollView import EmployeeListScrollView
from windows.widgets.WarehouseInfo import WarehouseInfoPanel

import kivy
from kivy.uix.boxlayout import BoxLayout

kivy.require('2.0.0')  # replace with your current kivy version !

# panel wyświetlający informacje o aktualnym stanie symulacji
class InfoPanel(BoxLayout):
    def __init__(self, sim, **kwargs):
        super(InfoPanel, self).__init__(**kwargs)

        self.orientation = 'vertical'

        self.employee_list_scroll_view = EmployeeListScrollView(sim)
        self.add_widget(self.employee_list_scroll_view)

        self.warehouse_info_panel = WarehouseInfoPanel()
        self.add_widget(self.warehouse_info_panel)