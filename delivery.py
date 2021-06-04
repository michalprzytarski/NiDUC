from math import fabs

import numpy
import simpy

DELIVERY_PRIORITY = 1           # priorytet dostaw


class Delivery:

    def __init__(self, tempo, warehouse, heap_time):
        self.warehouse = warehouse
        self.tempo = tempo
        self.delivery_items_queue = simpy.Container(warehouse.envi)     # przedmiotwy z dostawy oczekujące na odbiór
        self.priority = DELIVERY_PRIORITY
        self.heap_time=heap_time                                        # czas szczytu

    def force_delivery(self, delivery_size):
        yield self.warehouse.envi.timeout(0)
        print("Wymuszono dostawę ", delivery_size," przedmiotów")
        self.delivery_items_queue.put(delivery_size)
        self.warehouse.tasks.put(delivery_size)

    def generate_wait_period(self):
        while True:                                                     # imitacja petli do-while aby a != 0
            a = fabs(self.heap_time-self.warehouse.envi.now)
            if a != 0:
                break

        number_factor = 1 / a                                           # liczymy współczynnik, im dalej od szczytu tym większy
        extra_number = int(10 * number_factor)                          # w zależności od współczynnika liczymy dodatkową ilośc czasu do odczekania
        wait_period = int(numpy.random.normal(7, 2) + extra_number - self.tempo)
        if wait_period < 1:
            return 1
        else:
            return wait_period         # losujemy liczbe całkowitą z zadanego przedziału i dodajemy dodatkową ilość

    # generowanie losowego rozmiaru dostawy
    def generate_delivery_size(self):
        return int(numpy.random.normal(10, 2))                          # losowanie liczby całkowitej z rozkładu normalnego

    def run(self):
        while True:
            yield self.warehouse.envi.timeout(self.generate_wait_period())
            new_items = self.generate_delivery_size()                   # genrowanie rozmiaru dostawy
            print(new_items, "nowych przedmiotów z dostawy!(", self.warehouse.capacity-self.warehouse.items_stored.level, "wolnycyh miejsc,",self.delivery_items_queue.level + new_items, "przedmiotów do przeniesienia). Potrzebny pracownik do ich przeniesienia")
            self.delivery_items_queue.put(new_items)
            self.warehouse.tasks.put(new_items)
