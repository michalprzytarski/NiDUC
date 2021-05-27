
import simpy
import numpy
import break_time
import delivery
import issues
import orders
import employee
import forklift
import crash


class Warehouse:

    def __init__(self, capacity, start_items, environ):
        self.capacity = capacity                                        # pojemność magazynu
        self.items_stored = simpy.Container(environ, init=start_items,
                                            capacity=self.capacity)     # pojemnik na składowane towary
        self.envi = environ                                             # środowisko
        self.employees = []                                             # pracownicy
        self.orders_sent = 0                                            # liczba wysłanych zamównień
        self.items_received = 0                                         # liczba towarów otrzymanych z dostawy
        self.tasks = simpy.Container(environ)
        self.forklifts = []                                             # wózki widłowe
        self.breaks = None                                              # obiekt odpowiedzialny za przerwy
        self.crash = None                                               # obiekt odpowiedzialny za awarie
        self.idle = True                                                # brak pracy
        self.empty = False                                              # czy magazyn jest pusty
        self.issues = issues.Issues()                                   # zgloszone problemy

    # losowanie czasu oczekiwania
    def generate_wait_period(self):
        return numpy.random.exponential(15)                                         # losowa z rozkładu wykładniczego

    # dodawanie pracowików
    def hire_employees(self, num_of_employees, orders, delivery):
        for i in range(0, num_of_employees):
            yield self.envi.timeout(0.1)
            has_forklift_license = numpy.random.randint(1, 3)
            if has_forklift_license == 1:
                has_forklift_license = True
                emp_forklift = self.buy_forklift()
            else:
                has_forklift_license = False
                emp_forklift = None
            emp = employee.Employee(self, delivery, orders, has_forklift_license, emp_forklift)   # stworzenie obiektu pracownika
            self.employees.append(emp)
            print("Zatrudniono pracownika o id", emp.employee_id)

        # dodawanie wózków widłowych
    def buy_forklift(self):
        capacity = numpy.random.randint(5, 15)
        fork = forklift.Forklift(self, capacity)                                       # stworzenie obiektu wózka
        self.forklifts.append(fork)
        print("Kupiono wózek widłowy o nr", fork.forklift_id)
        return fork

    # generowanie dostaw
    def generate_deliveries(self, delivery):
        yield self.envi.timeout(0)
        self.envi.process(delivery.run())

    # generowanie zamówień
    def generate_orders(self, orders):
        yield self.envi.timeout(0)
        self.envi.process(orders.run())

    # generowanie przerw
    def generate_breaks(self, break_times, break_duration):
        yield self.envi.timeout(0)
        breaks = break_time.BreakTime(break_times, break_duration, self)
        self.breaks = breaks
        self.envi.process(breaks.run())

    def generate_crash(self, probability):
        yield self.envi.timeout(0)
        cr = crash.Crash(probability, self)
        self.crash = cr
        self.envi.process(cr.run())


#
#
#
# numpy.random.seed(0)
# env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)                    # stworzenie środkiska symulacji
# war = Warehouse(100, env)                                               # stworzenie obiektu magazynu
# delivery = delivery.Delivery(DELIVERY_TEMPO, war)                       # stworzenie obiektu dostaw
# orders = orders.Orders(ORDERS_TEMPO, war)                               # stworzenie obiektu zamówień
# # war.buy_forklifts(2)
#
# env.process(war.generate_breaks([20, 60], 15))                          # rozpoczecie procesu generowania przerw
# env.process(war.generate_deliveries(delivery))                          # rozpoczęcie procesu generowania dostaw
# env.process(war.generate_orders(orders))                                # rozpoczęcie procesu generowania zamówień
# env.process(war.hire_employees(3, orders, delivery))                    # dodanie pracowników
#
#
# env.run(until=200)
