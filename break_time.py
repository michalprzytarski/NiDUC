import simpy

from employee import Employee


class BreakTime:

    def __init__(self, break_times, break_duration, warehouse):
        self.break_times = break_times
        self.break_duration = break_duration
        self.is_it_breaktime = False
        self.last_break_time = 0
        self.warehouse = warehouse
        self.iterator = 0

    def run(self):
        while self.iterator < len(self.break_times):
            yield self.warehouse.envi.timeout(self.break_times[self.iterator] - self.warehouse.envi.now)
            self.is_it_breaktime = True
            self.last_break_time = self.warehouse.envi.now
            print("PRZERWA ! Pracownicy kończą swoje czynności i odpoczywają przez: ", self.break_duration)

            for e in self.warehouse.employees:
                if e.current_action is not None and e.waiting is True:
                    e.interrupt()
                    print("Przeszkodzono pracownikowi o id: ", e.employee_id)

            yield self.warehouse.envi.timeout(self.break_duration)
            print("KONIEC PRZERWY! Pracownicy wracają do pracy")
            self.is_it_breaktime = False
            self.iterator += 1
