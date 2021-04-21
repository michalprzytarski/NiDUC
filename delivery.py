import numpy


class Delivery:

    def __init__(self, tempo, warehouse):
        self.warehouse = warehouse
        self.tempo = tempo

    def generate_wait_period(self):
        return numpy.random.exponential(4)  # losowa z rozkładu wykładniczego

    def generate_delivery_size(self):
        return numpy.random.randint(1, 5)

    def run(self):
        while True:
            period = self.generate_wait_period()
            yield self.warehouse.envi.timeout(period)
            new_items = self.generate_delivery_size()
            # new_items += self.warehouse.delivery_queue
            # self.warehouse.delivery_queue = 0

            if (self.warehouse.items_stored + new_items) <= self.warehouse.capacity:  # enough space to take delivery
                print("New delivery: ", new_items, " items")

                while new_items > 0:
                    for emp in self.warehouse.list_of_employees:
                        if not emp.is_busy:
                            print("Employee ", emp.employee_id, " is taking delivery")
                            self.warehouse.envi.process(emp.take_delivery())
                            self.warehouse.items_stored += 1
                            new_items -= 1
                            break

            else:  # not enough space for all items in delivery
                print(new_items, " items in new delivery, but there is not enough space")

                free_space = self.warehouse.capacity - self.warehouse.items_stored
                while free_space > 0:
                    for emp in self.warehouse.list_of_employees:
                        if not emp.is_busy:
                            print("Employee ", emp.employee_id, " is taking delivery")
                            self.warehouse.envi.process(emp.take_delivery())
                            self.warehouse.items_stored += 1
                            new_items -= 1
                            free_space -= 1
                            break

                self.warehouse.delivery_queue += new_items
                print(self.warehouse.delivery_queue, " items in delivery queue")
