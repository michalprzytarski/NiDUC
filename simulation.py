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
        self.num_of_employees = 0 #liczba pracowników

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
        else:
            print("Nie wszystkie elmenty symualcji zostały zainicjowane!")

    def init_environment(self, simulation_tempo):
        self.env = simpy.rt.RealtimeEnvironment(simulation_tempo)  # stworzenie środkiska symulacji
        self.env_inited = True

    def init_warhouse(self, capacity, start_items):
        self.war = warehouse.Warehouse(capacity, start_items, self.env)  # stworzenie obiektu magazynu
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

    def test(self):
        print("test z symulacji")


#  sim = Simulation(100, 4, 1)
#  sim.run()

