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
        while True:
            self.is_busy = True
            # print(self.warehouse.envi.now, " Pracownik ", self.employee_id, " wysyla zamowienie")
            yield self.warehouse.envi.timeout(20/self.productivity)
            # print(self.warehouse.envi.now, " Pracownik ", self.employee_id, " skończył wysylać zamowienie")
            self.is_busy = False

    def take_delivery(self):
        while True:
            self.is_busy = True
            # print(self.warehouse.envi.now, " Pracownik ", self.employee_id, " odbiera towar")
            yield self.warehouse.envi.timeout(20/self.productivity)
            # print(self.warehouse.envi.now, " Pracownik ", self.employee_id, " skończył odbierać przedmiot z dostawy")
            self.is_busy = False

    def next_employee_id(self):
        global EMPLOYEE_ID
        EMPLOYEE_ID += 1
