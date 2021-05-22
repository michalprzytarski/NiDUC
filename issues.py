class Issues:

    def __init__(self):
        self.empty_war_count = 0
        self.idle_war_count = 0
        self.empty_war_times = []
        self.idle_war_times = []

    def warhouse_is_empty(self, current_time):
        self.empty_war_count += 1
        self.empty_war_times.append(current_time)
        print("Magazyn jest pusty! To ", self.empty_war_count, " taka sytuacja")

    def warhouse_is_idle(self, current_time):
        self.idle_war_count += 1
        self.idle_war_times.append(current_time)
        print("W magazynie brak jest jakichkolwiek zadan do wykonania! To ", self.idle_war_count, " taka sytuacja")

