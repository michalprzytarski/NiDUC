import numpy
import simpy
import delivery
import orders

import warehouse

SIMULATION_TEMPO = 10  # tempo symulacji
DELIVERY_TEMPO = 1  # tempo dostaw
ORDERS_TEMPO = 1  # tempo zamówień


class Simulation:

    def __init__(self, capacity, num_of_employees):
        self.env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)  # stworzenie środkiska symulacji
        self.war = warehouse.Warehouse(capacity, self.env)  # stworzenie obiektu magazynu
        self.delivery = delivery.Delivery(DELIVERY_TEMPO, self.war)  # stworzenie obiektu dostaw
        self.orders = orders.Orders(ORDERS_TEMPO, self.war)  # stworzenie obiektu zamówień
        self.num_of_employees = num_of_employees

    def run(self):
        # war.buy_forklifts(2)
        self.env.process(self.war.generate_breaks([50, 120], 15))  # rozpoczecie procesu generowania przerw
        self.env.process(self.war.generate_deliveries(self.delivery))  # rozpoczęcie procesu generowania dostaw
        self.env.process(self.war.generate_orders(self.orders))  # rozpoczęcie procesu generowania zamówień
        self.env.process(self.war.hire_employees(self.num_of_employees, self.orders, self.delivery))  # dodanie pracowników
        self.env.process(self.war.generate_crash(1))

        self.env.run(until=200)  # rozpoczęcie symulacji do zadanego czasu


sim = Simulation(100, 4)
sim.run()

