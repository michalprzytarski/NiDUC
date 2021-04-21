import numpy

EMPLOYEE_ID = 1


class Employee:

    def __init__(self, warehouse):
        self.is_busy = False
        self.productivity = 8
        # self.productivity = numpy.random.exponential(4)  # losowa z rozkladu wykladniczego
        self.warehouse = warehouse
        self.employee_id = EMPLOYEE_ID
        self.next_employee_id()

    def send_order(self):
        yield self.warehouse.envi.timeout(3)  # czas przeniesienia dostawy
        yield self.warehouse.items_stored.get(1) #tymczasowo po 1 przedmiocie
        yield self.warehouse.employees.put(self) #pracownik znowu jest wolny, wkładamy go do employees
        print("Pracownik ", self.employee_id, "zrealizował zamówienie i jest wolny")

    def take_delivery(self):
        yield self.warehouse.envi.timeout(3)  # czas przeniesienia dostawy
        yield self.warehouse.items_stored.put(1) #tymczasowo po 1 przedmiocie
        yield self.warehouse.employees.put(self)
        print("Pracownik ", self.employee_id, "przeniosl dostawe i jest wolny")

    def next_employee_id(self):
        global EMPLOYEE_ID
        EMPLOYEE_ID += 1
