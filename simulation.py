import numpy
import simpy
import delivery
import orders

import warehouse

DELIVERY_TEMPO = 1  # tempo dostaw
ORDERS_TEMPO = 1  # tempo zamówień


class Simulation:

    def __init__(self):
        self.env = None     #środkisko symulacji
        self.war = None     #magazyn
        self.delivery = None#dostawy
        self.orders = None  #zamówienia
        self.num_of_employees = 100 #liczba pracowników

        self.crash_probability = 1  #prawdopodobieństwo awarii
        self.break_times = [60, 120] #czasy przerw

        self.env_inited = False
        self.war_inited = False
        self.delivery_inited = False
        self.orders_inited = False

    def run(self):
        if self.env_inited and self.war_inited and self.delivery_inited and self.orders_inited:
            self.env.process(self.war.generate_breaks(self.break_times, 15))  # rozpoczecie procesu generowania przerw
            self.env.process(self.war.generate_deliveries(self.delivery))  # rozpoczęcie procesu generowania dostaw
            self.env.process(self.war.generate_orders(self.orders))  # rozpoczęcie procesu generowania zamówień
            self.env.process(self.war.hire_employees(self.num_of_employees, self.orders, self.delivery))  # dodanie pracowników
            self.env.process(self.war.generate_crash(self.crash_probability))

            self.env.run(until=200)  # rozpoczęcie symulacji do zadanego czasu
            print("ZAKONCZONO WATEK SYMULACJI!")
        else:
            print("Nie wszystkie elmenty symualcji zostały zainicjowane!")

    def init_environment(self, simulation_tempo):
        self.env = simpy.rt.RealtimeEnvironment(simulation_tempo, strict=False)  # stworzenie środkiska symulacji
        self.env_inited = True

    def init_warehouse(self, capacity, start_items):
        self.war = warehouse.Warehouse(capacity, start_items, self.env, 200)  # stworzenie obiektu magazynu
        self.war_inited = True

    def init_delivery(self, delivery_tempo, heap_time):
        self.delivery = delivery.Delivery(delivery_tempo, self.war, heap_time)  # stworzenie obiektu dostaw
        self.delivery_inited = True

    def init_orders(self, orders_tempo, heap_time):
        self.orders = orders.Orders(orders_tempo, self.war, heap_time)  # stworzenie obiektu zamówień
        self.orders_inited = True

    def set_employees_number(self, num_of_employees):
        self.num_of_employees = num_of_employees

    def set_crush_probability(self, probability):
        self.crash_probability = probability

    def add_break_time(self, break_time):
        self.break_times.append(break_time)

    def set_break_times(self, break_times):
        self.break_times = break_times

    def get_warehouse_occupation(self):
        occupation = self.war.items_stored.level / self.war.capacity
        return int(occupation * 100)

    def get_employees_tiredness(self):
        tiredness = 0
        for employee in self.war.employees:
            tiredness += employee.tiredness
        if len(self.war.employees) != 0:
            tiredness = tiredness // len(self.war.employees)
        return tiredness

    def get_deliveries_in_queue(self):
        return self.delivery.delivery_items_queue.level

    def get_orders_in_queue(self):
        return self.orders.orders_queue.level

    def get_is_crush(self):
        return self.war.crash.war_crashed

    def get_is_break(self):
        return self.war.breaks.is_it_breaktime

    def get_current_working(self):
        if len(self.war.employees) == 0:
            return 0
        current_working = 0
        for employee in self.war.employees:
            if not employee.waiting:
                current_working += 1
        return current_working / len(self.war.employees) * 100

    def add_orders(self, x):
        print('DODAJ 10 ZAMOWIEN')
        # yield self.env.timeout(0)
        # self.orders.orders_queue.put(10)
        # self.war.tasks.put(10)
        # yield self.env.process(self.orders.force_delivery(10))
        # self.env.process(self.orders.force_orders(10))
        self.orders.force_orders(10)
        # print('DODANO 10 ZAMOWIEN')

    def add_deliveries(self, x):
        print('DODAJ 10 DOSTAW')
        self.delivery.force_delivery(10)

sim = Simulation()
sim.init_environment(1)
sim.init_warehouse(1000, 5)
sim.init_orders(10,100)
sim.init_delivery(10, 100)
sim.run()

