import numpy
import simpy

DELIVERY_PRIORITY = 1           # priorytet dostaw


class Delivery:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo
        self.delivery_items_queue = simpy.Container(warehouse.envi)     # przedmiotwy z dostawy oczekujące na odbiór
        self.priority = DELIVERY_PRIORITY

    # generowanie losowego rozmiaru dostawy
    def generate_delivery_size(self):
        return numpy.random.randint(1, 5)                               # losowanie liczby całkowitej z zadanego przedziału

    def run(self):
            new_items = self.generate_delivery_size()                   # genrowanie rozmiaru dostawy
            print(new_items, "nowych przedmiotów z dostawy!(", self.warehouse.capacity-self.warehouse.items_stored.level, "wolnycyh miejsc,",self.delivery_items_queue.level + new_items, "przedmiotów do przeniesienia). Potrzebny pracownik do ich przeniesienia")
            self.delivery_items_queue.put(new_items)
            self.warehouse.tasks.put(new_items)
