import simpy
import numpy
import delivery
import orders
import employee

SIMULATION_TEMPO = 0.1
DELIVERY_TEMPO = 1
ORDERS_TEMPO = 1
START_ITEMS=0


class Warehouse:

    def __init__(self, capacity, environ):
        self.capacity = capacity
        self.items_stored = simpy.Container(environ, init=START_ITEMS, capacity=capacity)
        self.envi = environ
        self.employees = simpy.Store(self.envi, capacity=1000)


    def generate_wait_period(self):
        return numpy.random.exponential(15)  # losowa z rozkładu wykładniczego

    def hire_employees(self, num_of_employees):
        for i in range(0, num_of_employees):
            emp = employee.Employee(self)
            self.employees.put(emp)
            print("Hired employee ", emp.employee_id)

    def generate_deliveries(self, delivery):
        while True:
            period=self.generate_wait_period()
            yield self.envi.timeout(period)
            print("New delivery!")
            self.envi.process(delivery.run())

    def generate_orders(self,orders):
        while True:
            period= self.generate_wait_period()
            yield self.envi.timeout(period)
            print("Nowe zamówienia")
            self.envi.process(orders.run())


numpy.random.seed(0)
env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)
war = Warehouse(5, env)
war.hire_employees(3)
delivery = delivery.Delivery(DELIVERY_TEMPO, war)
orders = orders.Orders(ORDERS_TEMPO, war)
#deliveries=env.process(delivery.run())


env.process(war.generate_deliveries(delivery))
env.process(war.generate_orders(orders))

env.run(until=200)
