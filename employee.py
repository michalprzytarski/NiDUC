import random

import numpy

EMPLOYEE_ID = 1



class Employee:

    def __init__(self, warehouse):
        self.is_busy = False
        self.experience = random.randint(0, 9)    #doświadczenie pracownika, wpływa na produktywność
        self.tiredness = 0
        self.salary = 1000
        self.warehouse = warehouse
        self.employee_id = EMPLOYEE_ID
        self.next_employee_id()

    def send_order(self):
        yield self.warehouse.envi.timeout(3+(0.3*self.tiredness)**2-0.2*self.experience)  # czas przeniesienia dostawy
        yield self.warehouse.items_stored.get(1) #tymczasowo po 1 przedmiocie
        yield self.warehouse.employees.put(self) #pracownik znowu jest wolny, wkładamy go do employees
        self.warehouse.orders_sent += 1
        self.tiredness += 1
        print("Pracownik ", self.employee_id, "zrealizował zamówienie i jest wolny (zmęczenie:",self.tiredness, ")")

    def take_delivery(self):
        yield self.warehouse.envi.timeout(3+(0.3*self.tiredness)**2-0.2*self.experience)  # czas przeniesienia dostawy
        yield self.warehouse.items_stored.put(1) #tymczasowo po 1 przedmiocie
        yield self.warehouse.employees.put(self)
        self.warehouse.items_received += 1
        self.tiredness += 1
        print("Pracownik ", self.employee_id, "przeniosl dostawe i jest wolny (zmęczenie:",self.tiredness, ")")

    def next_employee_id(self):
        global EMPLOYEE_ID
        EMPLOYEE_ID += 1
