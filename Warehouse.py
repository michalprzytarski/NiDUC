import simpy
import numpy


class Warehouse():

    def __init__(self, capacity):

        self.capacity= capacity
        self.itemsStored=10
        self.queue=0

    #generowanie czasu
    def generatePeriod(self):
        return numpy.random.exponential(1./5)

    def generateOrders(self):
        return numpy.random.randint(1,5)


    def run(self):
        while True:
            period = self.generatePeriod()
            yield env.timeout(period)
            demand = self.generateOrders()

            if self.itemsStored > demand:
                self.itemsStored -= demand
                print(demand, " new orders!")

            else:
                print(demand, " new orders! but not enough items in warehouse")
                demand -= self.itemsStored
                self.itemsStored = 0
                self.queue += demand
                print(self.queue, " orders in queue\n")







numpy.random.seed(0)

env = simpy.Environment()
war=Warehouse(10)
env.process(war.run())
env.run(until=5.0)