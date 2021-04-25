import numpy


class Delivery:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo

    def generate_delivery_size(self):
        return numpy.random.randint(1, 5)

    def run(self):
            new_items = self.generate_delivery_size()
            print(new_items, " nowych przedmiotów z dostawy!(",self.warehouse.capacity-self.warehouse.items_stored.level, " wolnycyh miejsc) Potrzebny pracownik do ich przeniesienia")
            for i in range(new_items):
                employee = yield self.warehouse.employees.get()
                print("Znaleziono wolnego pracownika", employee.employee_id, "do przeniesienia dostawy!")
                self.warehouse.envi.process(employee.take_delivery())


