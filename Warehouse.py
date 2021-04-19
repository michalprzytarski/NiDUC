import simpy
import numpy
import Delivery
import Orders

SIMULATION_TEMPO=0.1
DELIVERY_TEMPO=1
ORDERS_TEMPO=1

class Warehouse():

    def __init__(self, capacity,env):

        self.capacity= capacity
        self.itemsStored=10
        self.queue=0
        self.env=env






numpy.random.seed(0)
env = simpy.rt.RealtimeEnvironment(SIMULATION_TEMPO)
war = Warehouse(10, env)
delivery = Delivery.Delivery(DELIVERY_TEMPO, war)
orders = Orders.Orders(ORDERS_TEMPO, war)
env.process(delivery.run())
env.process(orders.run())
env.run(until=100)