import simpy
import numpy
import delivery
import orders
import employee

SIMULATION_TEMPO = 0.1
DELIVERY_TEMPO = 1
ORDERS_TEMPO = 1


class Warehouse:

    list_of_employees = []

    def __init__(self, capacity, environ):
        self.capacity = capacity
        self.items_stored = 0
        self.orders_queue = 0
        self.delivery_queue = 0
        self.envi = environ

    def hire_employees(self, num_of_employees):
        for i in range(0, num_of_employees):
            self.list_of_employees.append(employee.Employee(self))


numpy.random.seed(0)
env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)
war = Warehouse(10, env)
war.hire_employees(10)
delivery = delivery.Delivery(DELIVERY_TEMPO, war)
orders = orders.Orders(ORDERS_TEMPO, war)
env.process(delivery.run())
env.process(orders.run())
env.run(until=50)
