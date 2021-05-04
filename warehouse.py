import simpy
import numpy
import delivery
import orders
import employee

SIMULATION_TEMPO = 0.1  # tempo symulacji
DELIVERY_TEMPO = 1  # tempo dostaw
ORDERS_TEMPO = 1  # tempo zamówień
START_ITEMS = 0  # liczba początkowych towarów
BREAK_TIME = 20  # czas po jakim nastąpi przerwa
BREAK_DURATION = 5  # czas trwania przerwy TODO: Przenieść do osobnego obiektu


class Warehouse:

    def __init__(self, capacity, environ):
        self.capacity = capacity  # pojemność magazynu
        self.items_stored = simpy.Container(environ, init=START_ITEMS,
                                            capacity=self.capacity)  # pojemnik na składowane towary
        self.envi = environ  # środowisko
        self.employees = simpy.Store(self.envi, capacity=1000)  # "przechowywalnia" na pracowników (przechowuje obiekty)
        self.orders_sent = 0  # liczba wysłanych zamównień
        self.items_received = 0  # liczba towarów otrzymanych z dostawy
        self.break_time = self.envi.event()  # wydarzenie przerwy TODO: przenieść do osobnego obiektu

    # losowanie czasu oczekiwania
    def generate_wait_period(self):
        return numpy.random.exponential(15)  # losowa z rozkładu wykładniczego

    # dodawanie pracowików
    def hire_employees(self, num_of_employees):
        for i in range(0, num_of_employees):
            emp = employee.Employee(self)  # stworzenie obiektu pracownika
            self.employees.put(emp)  # dodatnie utworzonego pracownika do wszystkich pracowników
            print("Dodano pracownika o id: ", emp.employee_id)

    # generowanie dostaw
    def generate_deliveries(self, delivery):
        while True:
            period = self.generate_wait_period()  # wylosowanej ilości czasu do odczekania
            yield self.envi.timeout(period)  # odczekanie wylosowanej ilości czasu
            print("New delivery!")
            self.envi.process(delivery.run())  # wystartowanie procesu dostawy

    # generowanie zamówień
    def generate_orders(self, orders):
        while True:
            period = self.generate_wait_period()  # wylosowanie ilości czasu do odczekania
            yield self.envi.timeout(period)  # odczekanie wylosowanej ilości czasu
            print("Nowe zamówienia")
            self.envi.process(orders.run())  # wystartowanie procesu zamówień

    # generowanie przerw
    def generate_breaks(self, breakTime):
        while True:
            yield self.envi.timeout(BREAK_TIME)

    # przerwa TODO: Przenieść do osobnego obiektu
    def breakTime(self):
        self.envi.timeout(BREAK_DURATION)


numpy.random.seed(0)
env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)  # stworzenie środkiska symulacji
war = Warehouse(1000, env)  # stworzenie obiektu magazynu
war.hire_employees(3)  # dodanie pracowników
delivery = delivery.Delivery(DELIVERY_TEMPO, war)  # stworzenie obiektu dostaw
orders = orders.Orders(ORDERS_TEMPO, war)  # stworzenie obiektu zamówień
# deliveries=env.process(delivery.run())


env.process(war.generate_deliveries(delivery))  # rozpoczęcie procesu generowania dostaw
env.process(war.generate_orders(orders))  # rozpoczęcie procesu generowania zamówień

env.run(until=200)  # rozpoczęcie symulacji do zadanego czasu

