from math import fabs

import numpy
import simpy

ORDERS_PRIORITY = 0             # priorytet zamówień


class Orders:

    def __init__(self, tempo, warehouse, heap_time):
        self.warehouse = warehouse
        self.tempo = tempo
        self.orders_queue = simpy.Container(warehouse.envi)             # zamówienia oczekujące na realizację
        self.priority = ORDERS_PRIORITY
        self.heap_time = heap_time                                      # czas szczytu zamówień

    def force_orders(self, number_of_orders):
        # yield self.warehouse.envi.timeout(0)
        print('Wymuszono', number_of_orders, ' nowych zamowien')
        self.orders_queue.put(10)
        self.warehouse.tasks.put(10)
        
    # generowanie losowej liczby całkowitej dla ilości zamówień
    def generate_order_number(self):
        while True:                                                             # imitacja petli do-while aby a != 0
            a = fabs(self.heap_time-self.warehouse.envi.now)
            if a != 0:
                break

        number_factor = 1/a                                                     # liczymy współczynnik, im dalej od szczytu tym mniejszy
        extra_number = int(10*number_factor)                                    # w zależności od współczynnika liczymy dodatkową ilośc zamówień (max.10)
        return int(numpy.random.randint(3, 8) + extra_number)                   # losujemy liczbe całkowitą z zadanego przedziału i dodajemy dodatkową ilość

    def generate_wait_period(self):
        wait_period = numpy.random.normal(7-self.tempo, 2)
        if(wait_period<1):
            return 1
        else:
            return wait_period                                # losowa liczba z rozkładu normalnego (loc, scale, size)

    def run(self):
        while True:
            yield self.warehouse.envi.timeout(self.generate_wait_period())
            new_orders = self.generate_order_number()                           # generujemy liczbe zamówień
            print(new_orders, "nowych zamówień!(", self.orders_queue.level+new_orders, "oczekujacych zamówień). Potrzebny pracownik/cy do ich realizacji")
            self.orders_queue.put(new_orders)
            self.warehouse.tasks.put(new_orders)
