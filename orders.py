import numpy


class Orders:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo

    def generate_wait_period(self):
        return numpy.random.exponential(4)

    def generate_order_number(self):
        return numpy.random.randint(1, 5)

    def run(self):
        while True:
            period = self.generate_wait_period()
            yield self.warehouse.envi.timeout(period)
            new_orders = self.generate_order_number()
            # new_orders += self.warehouse.orders_queue
            # self.warehouse.orders_queue = 0

            if self.warehouse.items_stored >= new_orders:  # enough items to send all orders
                print(new_orders, " new orders")

                while new_orders > 0:
                    i = 0
                    while i < len(self.warehouse.list_of_employees):
                        if not self.warehouse.list_of_employees[i].is_busy:
                            print("Employee ", self.warehouse.list_of_employees[i].employee_id, " is sending order")
                            self.warehouse.envi.process(self.warehouse.list_of_employees[i].send_order())
                            self.warehouse.items_stored -= 1
                            new_orders -= 1
                            break

                        i += 1

            else:  # not enough stored items
                print(new_orders, " new orders, but there is not enough items stored")

                while self.warehouse.items_stored > 0:
                    i = 0
                    while i < len(self.warehouse.list_of_employees):
                        if not self.warehouse.list_of_employees[i].is_busy:
                            print("Employee ", self.warehouse.list_of_employees[i].employee_id, " is sending order")
                            self.warehouse.envi.process(self.warehouse.list_of_employees[i].send_order())
                            self.warehouse.items_stored -= 1
                            new_orders -= 1
                            break

                        i += 1

                self.warehouse.orders_queue += new_orders
                print(self.warehouse.orders_queue, " orders in queue")
