import csv
import random
import time


class DataWriter:
    def __init__(self, filename):
        self.file_name = '../data/' + filename + '.csv' #../data/warehouse_occupation.csv'

        self.sim_time = 0
        self.occupation_value = 0
        self.current_working_value = 0

        self.fieldnames = ["sim_time", "occupation_value", "current_working_value"]

        with open(self.file_name, 'w') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)
            csv_writer.writeheader()

    def add_new_data(self, sim_time_to_add, occupation_to_add, working_to_add):
        with open(self.file_name, 'a') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=self.fieldnames)

            info = {
                "sim_time": self.sim_time,
                "occupation_value": self.occupation_value,
                "current_working_value": self.current_working_value
            }

            csv_writer.writerow(info)
            # print(x_value, y_value,)

            self.sim_time = sim_time_to_add
            self.occupation_value = occupation_to_add # self.y_value + random.randint(-6, 8)
            self.current_working_value = working_to_add

        # time.sleep(1)