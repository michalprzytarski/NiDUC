from windows.widgets.EmployeeListGrid import EmployeeListGrid

import kivy
from kivy.uix.scrollview import ScrollView

kivy.require('2.0.0')  # replace with your current kivy version !

# skrolowalna lista pracowników wraz z inforamacjami o nich
class EmployeeListScrollView(ScrollView):
    def __init__(self, sim, **kwargs):
        super(EmployeeListScrollView, self).__init__(**kwargs)

        # Dodanie styli do klasy
        self.size_hint_y = 1
        self.do_scroll_x = False
        self.do_scroll_y = True

        self.employee_list_grid = EmployeeListGrid(sim)
        self.employee_list_grid.bind(minimum_height=self.employee_list_grid.setter('height'))
        self.add_widget(self.employee_list_grid)