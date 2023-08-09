import random
from datetime import datetime

class Sensor:
## create a class that simulate a sensor (a class that generate a random data), the data should be send with the timestamp
    def __init__(self, min_value, max_value):
        self.min_value = min_value
        self.max_value = max_value
    def read_data(self):
        return [datetime.now(), random.uniform(self.min_value, self.max_value)]