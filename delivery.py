import numpy



class Delivery():

    def __init__(self,tempo,warehouse):
        self.warehouse=warehouse
        self.tempo=tempo

    def generateWaitPeriod(self):
        return numpy.random.exponential(4)  # losowa z rozkładu wykładniczego

    def generateDeliverySize(self):
        return numpy.random.randint(1, 5)

    def run(self):
        while True:
            period = self.generateWaitPeriod()
            yield self.warehouse.env.timeout(period)
            newItems = self.generateDeliverySize()
            print(newItems," nowych towarów przybyło do magazynu")
            self.warehouse.itemsStored+=newItems
