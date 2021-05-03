import numpy
import simpy

class Orders:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo

    # generowanie losowej liczby całkowitej dla ilości zamówień
    def generate_order_number(self):
        return numpy.random.randint(1, 4)                               # losujemy liczbe całkowitą z zadanego przedziału

    def run(self):
            new_orders = self.generate_order_number()                   # generujemy liczbe zamówień
            print(new_orders, " nowych zamówień!(",self.warehouse.items_stored.level, " przedmiotów w magazynie) Potrzebny pracownik do ich realizacji")
            for i in range(new_orders):                                 # dla każdego zamówienia szukamy pracownika do jego realizacji
                employee = yield self.warehouse.employees.get()         # pobieramy pracownika z póli pracowników (jezeli jakiś jest, jeżeli nie czekamy)
                print("Pracownik ", employee.employee_id, "realizuje 1 zamówienie!")
                self.warehouse.envi.process(employee.send_order())      # startujemy proces ralizacji zamówienia przez pracownika
