import random

import numpy

EMPLOYEE_ID = 1     # id dla pracownika



class Employee:

    def __init__(self, warehouse):
        self.experience = random.randint(0, 9)      # doświadczenie pracownika, wpływa na produktywność
        self.tiredness = 0                          # poziom zmęczenia pracownika
        self.salary = 1000                          # wypłata pracownika
        self.warehouse = warehouse
        self.employee_id = EMPLOYEE_ID              # id pracownika
        self.next_employee_id()                     # inkrementacja id dla następnego pracownika

    # realizacja zamówienia
    def send_order(self):
        yield self.warehouse.envi.timeout(3+(0.3*self.tiredness)**2-0.2*self.experience)    # wyliczamy czas realizacji zamówienia i odczekujemy go
        yield self.warehouse.items_stored.get(1)                                            # pobieramy przedmiot z magazynu (tymczasowo po 1 przedmiocie)
        yield self.warehouse.employees.put(self)                                            # pracownik znowu jest wolny, odkładamy go do employees
        self.warehouse.orders_sent += 1
        self.tiredness += 1
        print("Pracownik ", self.employee_id, "zrealizował zamówienie i jest wolny (zmęczenie:",self.tiredness, ")")

    # odebranie towaru
    def take_delivery(self):
        yield self.warehouse.envi.timeout(3+(0.3*self.tiredness)**2-0.2*self.experience)    # wyliczamy czas przeniesienia dostawy
        yield self.warehouse.items_stored.put(1)                                            # odkładamy przedmiot do magazynu tymczasowo po 1 przedmiocie
        yield self.warehouse.employees.put(self)                                            # pracownik znowu jest wolny, odkładamy go do employees
        self.warehouse.items_received += 1
        self.tiredness += 1
        print("Pracownik ", self.employee_id, "przeniosl dostawe i jest wolny (zmęczenie:",self.tiredness, ")")

    # inkrementacja id
    def next_employee_id(self):
        global EMPLOYEE_ID
        EMPLOYEE_ID += 1