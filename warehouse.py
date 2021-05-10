import simpy
import numpy
import break_time
import delivery
import orders
import employee
import forklift

SIMULATION_TEMPO = 0.1          # tempo symulacji
DELIVERY_TEMPO = 1              # tempo dostaw
ORDERS_TEMPO = 1                # tempo zamówień
START_ITEMS = 0                 # liczba początkowych towarów


class Warehouse:

    def __init__(self, capacity, environ):
        self.capacity = capacity                                        # pojemność magazynu
        self.items_stored = simpy.Container(environ, init=START_ITEMS,
                                            capacity=self.capacity)     # pojemnik na składowane towary
        self.envi = environ                                             # środowisko
        self.employees = []                                             # pracownicy
        self.forklifts = simpy.Store(self.envi, capacity=1000)          # wózki widłowe
        self.orders_sent = 0                                            # liczba wysłanych zamównień
        self.items_received = 0                                         # liczba towarów otrzymanych z dostawy
        self.tasks = simpy.Container(environ)
        self.breaks = 0                                                 # obiekt odpowiedzialny za przerwy

    # losowanie czasu oczekiwania
    def generate_wait_period(self):
        return numpy.random.exponential(15)                             # losowa z rozkładu wykładniczego

    # dodawanie pracowików
    def hire_employees(self, num_of_employees, orders, delivery):
        for i in range(0, num_of_employees):
            yield self.envi.timeout(0.1)
            emp = employee.Employee(self, delivery, orders)             # stworzenie obiektu pracownika
            self.employees.append(emp)
            print("Zatrudniono pracownika o id", emp.employee_id)

    # dodawanie wózków widłowych
    def buy_forklifts(self, num_of_forklifts):
        for i in range(0, num_of_forklifts):
            yield self.envi.timeout(0.1)
            fork = forklift.Forklift(self, 3)                           # stworzenie obiektu wózka
            self.forklifts.put(fork)
            print("Kupiono wózek widłowy o nr", fork.forklift_id)

    # generowanie dostaw
    def generate_deliveries(self, delivery):
        while True:
            period = self.generate_wait_period()                        # wylosowanej ilości czasu do odczekania
            yield self.envi.timeout(period)                             # odczekanie wylosowanej ilości czasu
            print("Nowa dostawa!")
            delivery.run()                                              # wystartowanie procesu dostawy

    # generowanie zamówień
    def generate_orders(self, orders):
        while True:
            period = self.generate_wait_period()                        # wylosowanie ilości czasu do odczekania
            yield self.envi.timeout(period)                             # odczekanie wylosowanej ilości czasu
            print("Nowe zamówienia")
            orders.run()                                                # wystartowanie procesu zamówień

    # generowanie przerw
    def generate_breaks(self, break_times, break_duration):
        yield self.envi.timeout(0)
        breaks = break_time.BreakTime(break_times, break_duration, self)
        self.breaks = breaks
        self.envi.process(breaks.run())


numpy.random.seed(0)
env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)                    # stworzenie środkiska symulacji
war = Warehouse(100, env)                                               # stworzenie obiektu magazynu
delivery = delivery.Delivery(DELIVERY_TEMPO, war)                       # stworzenie obiektu dostaw
orders = orders.Orders(ORDERS_TEMPO, war)                               # stworzenie obiektu zamówień

# deliveries=env.process(delivery.run())
env.process(war.buy_forklifts(2))
env.process(war.generate_breaks([20, 40], 15))                          # rozpoczecie procesu generowania przerw
env.process(war.generate_deliveries(delivery))                          # rozpoczęcie procesu generowania dostaw
env.process(war.generate_orders(orders))                                # rozpoczęcie procesu generowania zamówień
env.process(war.hire_employees(5, orders, delivery))                    # dodanie pracowników


env.run(until=200)                                                      # rozpoczęcie symulacji do zadanego czasu
