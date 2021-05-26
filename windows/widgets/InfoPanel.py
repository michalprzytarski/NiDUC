from windows.widgets.EmployeeListScrollView import EmployeeListScrollView
from windows.widgets.WarehouseInfo import WarehouseInfoPanel
from windows.widgets.EmployeeListLabel import EmployeeListLabel

import kivy
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

kivy.require('2.0.0')  # replace with your current kivy version !

# panel wyświetlający informacje o aktualnym stanie symulacji
class InfoPanel(BoxLayout):
    def __init__(self, sim, **kwargs):
        super(InfoPanel, self).__init__(**kwargs)

        self.orientation = 'vertical'

        # Dodanie sekcji z nazwami kolumn wyświetlanych w employee_list_scroll_view
        self.employee_list_column_names = GridLayout()
        self.employee_list_column_names.add_widget(EmployeeListLabel(text='Id pracownika', color=(1, 1, 0, 1)))
        self.employee_list_column_names.add_widget(EmployeeListLabel(text='Doświadczenie', color=(1, 1, 0, 1)))
        self.employee_list_column_names.add_widget(EmployeeListLabel(text='Status', color=(1, 1, 0, 1)))
        self.employee_list_column_names.add_widget(EmployeeListLabel(text='Zmęczenie', color=(1, 1, 0, 1)))
        # Stylizowanie sekcji z nazwami kolumn
        self.height = self.minimum_height
        self.employee_list_column_names.row_default_height = 20
        self.employee_list_column_names.size_hint_y = 0.1
        self.employee_list_column_names.cols = 4
        self.employee_list_column_names.spacing = 10
        self.employee_list_column_names.padding = 10
        self.add_widget(self.employee_list_column_names)

        # Dodanie przewijalnej sekcji z tabelą informacji o pracownikach
        self.employee_list_scroll_view = EmployeeListScrollView(sim)
        self.add_widget(self.employee_list_scroll_view)

        # Dodanie polnego panelu z podsumowaniem informacji o magazynie
        self.warehouse_info_panel = WarehouseInfoPanel()
        self.add_widget(self.warehouse_info_panel)
