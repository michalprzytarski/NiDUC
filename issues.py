
class Issues:

     def __init__(self):
         self.empty_war_count = 0
         self.idle_war_count = 0

     def warhouse_is_empty(self):
         self.empty_war_count +=1
         print("Magazyn jest pusty! To ", self.empty_war_count, " taka sytuacja")

     def warhouse_is_idle(self):
         self.idle_war_count += 1
         print("W magazynie brak jest jakichkolwiek zadan do wykonania! To ", self.idle_war_count, " taka sytuacja")



