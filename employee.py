import random
import simpy
import numpy

EMPLOYEE_ID = 1  # id dla pracownika


class Employee:

    def __init__(self, warehouse, delivery, orders, has_forklift_license, emp_forklift):
        self.experience = random.randint(0, 9)                          # doświadczenie pracownika, wpływa na produktywność
        self.tiredness = 0                                              # poziom zmęczenia pracownika
        self.salary = 1000                                              # wypłata pracownika
        self.warehouse = warehouse
        self.employee_id = EMPLOYEE_ID                                  # id pracownika
        self.next_employee_id()                                         # inkrementacja id dla następnego pracownika
        self.delivery = delivery                                        # obiekt dostaw
        self.orders = orders                                            # obiekt zamówień
        self.idle_time = 0                                              # ilość czasu w którym pracownik nie wykonywał pracy
        self.tasks_completed = 0                                        # wykonane zadania
        self.current_action = self.warehouse.envi.process(self.run())   # wykonywane aktualnie zadanie
        self.waiting = False
        self.has_forklift_license = has_forklift_license                # czy posiada uprawnienia na wózek widłowy
        self.forklift = emp_forklift                                    # jeśli ma uprawnienia to ma przypisany wózek

    def run(self):
        while True:
            if self.warehouse.breaks.is_it_breaktime:
                yield self.warehouse.envi.process(self.go_on_break())
            if self.warehouse.crash.war_crashed:
                yield self.warehouse.envi.process(self.wait_for_fix())
            else:
                self.waiting = True
                try:
                    idle_time_start = self.warehouse.envi.now  # rozpoczęcie pomiaru czasu bezczynności
                    yield self.warehouse.tasks.get(1)  # czekanie na zadanie
                    self.idle_time += self.warehouse.envi.now - idle_time_start  # koniec pomiaru czasu bezczynności
                except simpy.Interrupt:
                    if self.warehouse.breaks.is_it_breaktime:
                        yield self.warehouse.envi.process(self.go_on_break())
                    if self.warehouse.crash.war_crashed:
                        yield self.warehouse.envi.process(self.wait_for_fix())
                self.waiting = False

                if self.orders.priority > self.delivery.priority or (
                        self.orders.orders_queue.level > 0 and
                        self.warehouse.items_stored.level > 0 and
                        self.delivery.delivery_items_queue.level < 1):
                    if self.has_forklift_license:
                        items_to_send = min(self.warehouse.items_stored.level, self.forklift.capacity, self.orders.orders_queue.level)
                    else:
                        items_to_send = min(self.warehouse.items_stored.level, 1, self.orders.orders_queue.level)

                    if items_to_send == 0:
                        continue
                    yield self.orders.orders_queue.get(items_to_send)
                    self.warehouse.idle = False
                    yield self.warehouse.envi.process(self.send_order(items_to_send))
                else:
                    if self.has_forklift_license:
                        items_to_take = min((self.warehouse.capacity - self.warehouse.items_stored.level),
                                            self.forklift.capacity, self.delivery.delivery_items_queue.level)
                    else:
                        items_to_take = min((self.warehouse.capacity - self.warehouse.items_stored.level),
                                            1, self.delivery.delivery_items_queue.level)

                    if items_to_take == 0:
                        continue
                    yield self.delivery.delivery_items_queue.get(items_to_take)
                    self.warehouse.idle = False
                    yield self.warehouse.envi.process(self.take_delivery(items_to_take))
                    self.warehouse.empty = False
            yield self.warehouse.envi.process(self.report_issues())

    def wait_for_fix(self):
        print("Pracownik", self.employee_id, "czeka na koniec awarii")
        yield self.warehouse.envi.timeout(self.warehouse.crash.crash_duration - (
                self.warehouse.envi.now - self.warehouse.crash.last_crash_time))  # awaria
        print("Pracownik", self.employee_id, "wraca do pracy po awarii")

    # przerwa!
    def go_on_break(self):
        print("Pracownik", self.employee_id, "idzie na przerwe")
        yield self.warehouse.envi.timeout(self.warehouse.breaks.break_duration - (
                self.warehouse.envi.now - self.warehouse.breaks.last_break_time))  # przerwa
        print("Pracownik", self.employee_id, "wraca z przerwy")
        self.tiredness -= self.warehouse.breaks.break_duration * 2
        if self.tiredness < 0:
            self.tiredness = 0

    def interrupt(self):
        self.current_action.interrupt()

    # realizacja zamówienia
    def send_order(self, items_to_send):
        if self.has_forklift_license:
            fork_info = f"za pomocą wózka widłowego nr {self.forklift.forklift_id}"
        else:
            fork_info = ""

        print("Pracownik", self.employee_id, "realizuje", items_to_send, "zamówienie/a", fork_info)
        if items_to_send > 1:
            yield self.warehouse.tasks.get(items_to_send - 1)
        yield self.warehouse.envi.timeout(3 + (
                    0.3 * self.tiredness) ** 2 - 0.2 * self.experience)  # wyliczamy czas realizacji zamówienia i odczekujemy go
        yield self.warehouse.items_stored.get(items_to_send)  # pobieramy przedmiot z magazynu
        self.warehouse.orders_sent += items_to_send
        self.tiredness += 1
        self.tasks_completed += items_to_send
        print("Pracownik", self.employee_id, "zrealizował zamówienie i jest wolny (zmęczenie:", self.tiredness, ")")

    # odebranie towaru
    def take_delivery(self, items_to_take):
        if self.has_forklift_license:
            fork_info = f"za pomocą wózka widłowego nr {self.forklift.forklift_id}"
        else:
            fork_info = ""

        print("Pracownik", self.employee_id, "przenosi", items_to_take, "przedmiot/y z dostawy", fork_info)
        if items_to_take > 1:
            yield self.warehouse.tasks.get(items_to_take - 1)
        yield self.warehouse.envi.timeout(
            3 + (0.3 * self.tiredness) ** 2 - 0.2 * self.experience)  # wyliczamy czas przeniesienia dostawy
        yield self.warehouse.items_stored.put(
            items_to_take)  # odkładamy przedmiot do magazynu tymczasowo po 1 przedmiocie
        self.warehouse.items_received += items_to_take
        self.tiredness += 1
        self.tasks_completed += items_to_take
        print("Pracownik", self.employee_id, "przeniosl dostawe i jest wolny (zmęczenie:", self.tiredness, ")")

    # zgłoszenie problemów/sytuacji wyjątkowych (jeżeli jakieś wystąpiły)
    def report_issues(self):
        yield self.warehouse.envi.timeout(0)
        if self.warehouse.items_stored.level == 0 and self.warehouse.empty == False:
            self.warehouse.issues.warhouse_is_empty(self.warehouse.envi.now)
            self.warehouse.empty = True
        if self.warehouse.tasks.level == 0 and self.warehouse.idle == False:
            self.warehouse.issues.warhouse_is_idle(self.warehouse.envi.now)
            self.warehouse.idle = True

    # inkrementacja id
    def next_employee_id(self):
        global EMPLOYEE_ID
        EMPLOYEE_ID += 1
