import numpy
import warehouse

class Crash:

    def __init__(self, probability, war):
        self.probability = probability
        self.war_crashed = False
        self.warehouse = war
        self.crash_duration = None
        self.last_crash_time = None

    def generate_random_number(self):
        self.warehouse.envi.timeout(0)
        return numpy.random.randint(0, 100)

    def generate_crash_time_duration(self):
        self.warehouse.envi.timeout(0)
        return numpy.random.exponential(15)+2   #wart agrumentu  = beta = 1/lambda

    def run(self):
        while True:
            yield self.warehouse.envi.timeout(5)
            random_number=self.generate_random_number()
            if (random_number > 100 - self.probability) and not self.war_crashed:
                self.war_crashed = True
                self.last_crash_time = self.warehouse.envi.now
                crash_duration = self.generate_crash_time_duration()
                self.crash_duration = crash_duration
                print("Awaria!")
                for e in self.warehouse.employees:
                    if e.current_action is not None and e.waiting is True:
                        e.interrupt()
                        print("Przeszkodzono pracownikowi o id: ", e.employee_id)

                yield self.warehouse.envi.timeout(crash_duration)
                print("Awaria naprawiona!")
                self.war_crashed = False


