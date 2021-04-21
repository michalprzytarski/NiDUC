import numpy
import simpy

class Orders:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo


    def generate_order_number(self):
        return numpy.random.randint(1, 4)

    def run(self):
            new_orders = self.generate_order_number()
            print(new_orders, " nowych zamówień! Potrzebny pracownik do ich realizacji")
            for i in range(new_orders):
                employee = yield self.warehouse.employees.get()
                print("Znaleziono wolnego pracownika (", employee.employee_id, ")do realizacji zamówienia!")
                self.warehouse.envi.process(employee.send_order())
