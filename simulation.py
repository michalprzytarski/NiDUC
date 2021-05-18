import numpy
import simpy
import delivery
import orders

import warehouse

SIMULATION_TEMPO = 1  # tempo symulacji
DELIVERY_TEMPO = 1  # tempo dostaw
ORDERS_TEMPO = 1  # tempo zamówień


class Simulation:

    def __init__(self, capacity, num_of_employees, start_items, break_times, delivery_tempo, order_tempo):
        self.break_times=break_times
        self.delivery_tempo=delivery_tempo
        self.order_tempo = order_tempo
        self.env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)  # stworzenie środkiska symulacji
        self.war = warehouse.Warehouse(capacity, self.env, start_items)  # stworzenie obiektu magazynu
        self.delivery = delivery.Delivery(self.war)  # stworzenie obiektu dostaw
        self.orders = orders.Orders(self.war)  # stworzenie obiektu zamówień
        self.num_of_employees = num_of_employees

    def run(self):
        # war.buy_forklifts(2)
        self.env.process(self.war.generate_breaks(self.break_times, 15))  # rozpoczecie procesu generowania przerw
        self.env.process(self.war.generate_deliveries(self.delivery, self.delivery_tempo))  # rozpoczęcie procesu generowania dostaw
        self.env.process(self.war.generate_orders(self.orders, self.order_tempo))  # rozpoczęcie procesu generowania zamówień
        self.env.process(self.war.hire_employees(self.num_of_employees, self.orders, self.delivery))  # dodanie pracowników
        self.env.run(until=200)  # rozpoczęcie symulacji do zadanego czasu


sim = Simulation(100, 4, 0, [60,120], 1, 1)
sim.run()