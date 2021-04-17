import simpy
import numpy
TEMPO=0.1

class Warehouse():

    def __init__(self, capacity):

        self.capacity= capacity
        self.itemsStored=10
        self.queue=0

    #generowanie czasu
    def generatePeriod(self):
        return numpy.random.exponential(4)   # losowa z rozkładu wykładniczego

    def generateNumber(self):
        return numpy.random.randint(1,5)


    def generateOrders(self):
        while True:
            period = self.generatePeriod()
            yield env.timeout(period)
            newOrders = self.generateNumber()

            if self.itemsStored > newOrders:
                self.itemsStored -= newOrders
                print(newOrders, " nowe zamówienia!")

            else:
                print(newOrders, " nowych zamówień ale brak towaru do realizacji wszystkich!")
                newOrders -= self.itemsStored
                self.itemsStored = 0
                self.queue += newOrders
                print(self.queue, " zamówień w kolejce\n")

    def generateSupply(self):
        while True:
            period = self.generatePeriod()
            yield env.timeout(period)
            newItems = self.generateNumber()
            print(newItems," nowych towarów przybyło do magazynu")
            self.itemsStored+=newItems





numpy.random.seed(0)
env = simpy.rt.RealtimeEnvironment(TEMPO)
war=Warehouse(10)
env.process(war.generateOrders())
env.process(war.generateSupply())
env.run(until=100)