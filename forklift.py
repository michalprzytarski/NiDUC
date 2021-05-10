FORKLIFT_ID = 1         # id wózka widłowego


class Forklift:

    def __init__(self, warehouse, capacity):
        self.warehouse = warehouse          # magazyn
        self.capacity = capacity            # pojemność wózka
        self.forklift_id = FORKLIFT_ID      # id wózka
        self.next_forklift_id()             # inkrementacja id dla następnego wózka

    def next_forklift_id(self):
        global FORKLIFT_ID
        FORKLIFT_ID += 1
