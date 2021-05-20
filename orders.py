from math import fabs

import numpy
import simpy

ORDERS_PRIORITY = 0             # priorytet zamówień
HEAP = 100                      # czas szczytu zamówień


class Orders:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo
        self.orders_queue = simpy.Container(warehouse.envi)             # zamówienia oczekujące na realizację
        self.priority = ORDERS_PRIORITY

    # generowanie losowej liczby całkowitej dla ilości zamówień
    def generate_order_number(self):
        number_factor = 1/fabs(HEAP-self.warehouse.envi.now)                   # liczymy współczynnik, im dalej od szczytu tym mniejszy
        extra_number = int(10*number_factor)                                   # w zależności od współczynnika liczymy dodatkową ilośc zamówień (max.10)
        return int(numpy.random.randint(1, 4) + extra_number)                  # losujemy liczbe całkowitą z zadanego przedziału i dodajemy dodatkową ilość

    def generate_wait_period(self):
        return int(numpy.random.normal(5, 2))                                   # losowa liczba z rozkładu normalnego (loc, scale, size)

    def run(self):
        while True:
            yield self.warehouse.envi.timeout(self.generate_wait_period())
            new_orders = self.generate_order_number()                   # generujemy liczbe zamówień
            print(new_orders, "nowych zamówień!(",self.orders_queue.level+new_orders, "oczekujacych zamówień). Potrzebny pracownik/cy do ich realizacji")
            self.orders_queue.put(new_orders)
            self.warehouse.tasks.put(new_orders)
