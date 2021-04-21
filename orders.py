
import numpy



class Orders():

    def __init__(self,tempo,warehouse):
        self.warehouse=warehouse
        self.tempo=tempo

    def generateWaitPeriod(self):
        return numpy.random.exponential(4)  # losowa z rozkładu wykładniczego

    def generateOrderNumber(self):
        return numpy.random.randint(1, 5)

    def run(self):
        while True:
            period = self.generateWaitPeriod()
            yield self.warehouse.env.timeout(period)
            newOrders = self.generateOrderNumber()

            if self.warehouse.itemsStored > newOrders:
                self.warehouse.itemsStored -= newOrders
                print(newOrders, " nowe zamówienia!")

            else:
                print(newOrders, " nowych zamówień ale brak towaru do realizacji wszystkich!")
                newOrders -= self.warehouse.itemsStored
                self.warehouse.itemsStored=0
                self.warehouse.queue += newOrders
                print(self.warehouse.queue, " zamówień w kolejce\n")