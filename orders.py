import numpy
import simpy

ORDERS_PRIORITY = 0             # priorytet zamówień


class Orders:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo
        self.orders_queue = simpy.Container(warehouse.envi)             # zamówienia oczekujące na realizację
        self.priority = ORDERS_PRIORITY

    # generowanie losowej liczby całkowitej dla ilości zamówień
    def generate_order_number(self):
        return numpy.random.randint(1, 4)                               # losujemy liczbe całkowitą z zadanego przedziału

    def run(self):
            new_orders = self.generate_order_number()                   # generujemy liczbe zamówień
            print(new_orders, "nowych zamówień!(",self.orders_queue.level+new_orders, "oczekujacych zamówień). Potrzebny pracownik/cy do ich realizacji")
            self.orders_queue.put(new_orders)
            self.warehouse.tasks.put(new_orders)