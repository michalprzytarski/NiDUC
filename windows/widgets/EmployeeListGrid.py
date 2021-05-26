from windows.widgets.EmployeeListLabel import EmployeeListLabel

import kivy
from kivy.uix.gridlayout import GridLayout

kivy.require('2.0.0')  # replace with your current kivy version !

# panel znajdujący się w EmployeeListScrollView służący do porządkowania informacji o pracownikach
class EmployeeListGrid(GridLayout):
    def __init__(self, sim, **kwargs):
        super(EmployeeListGrid, self).__init__(**kwargs)

        self.height = self.minimum_height
        self.row_default_height = 20
        self.size_hint_y = None
        self.cols = 3
        self.spacing = 10
        #self.canvas = Canvas()
        #with self.canvas:
        #    Color(1, 1, 1)
        #    Rectangle(pos=self.pos, size=self.size)


        #for i in range(100):                                               # testowe dodawanie pól
        #    self.add_widget(EmployeeListLabel(text='Pracownik %s' % i))
        #    self.add_widget(EmployeeListLabel(text='wolny'))
        #    self.add_widget(EmployeeListLabel(text='zmęczenie :0'))

    def refresh_employee_grid(self, employees):
        # Wyczyszczenie aktualnej zawartości panelu
        self.clear_widgets()

        # Dodanie etykiet tabel
        self.add_widget(EmployeeListLabel(text='Id pracownika', color=(0, 1, 0, 1)))
        self.add_widget(EmployeeListLabel(text='Status', color=(0, 1, 0, 1)))
        self.add_widget(EmployeeListLabel(text='Zmęczenie', color=(0, 1, 0, 1)))

        # Dodanie aktualnych informacji o pracownikach
        for employee in employees:
            self.add_widget(EmployeeListLabel(text='%s' % employee.employee_id))
            self.add_widget(EmployeeListLabel(text='%s' % "Czeka" if employee.waiting else "Pracuje", color=((1, 0, 0, 1) if employee.waiting else (0, 1, 0, 1))))
            self.add_widget(EmployeeListLabel(text='%s' % employee.tiredness))
