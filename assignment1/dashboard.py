import random
from datetime import datetime

class Dashboard:
    # compelet this function to display the data
    def display_data(self, data):
        print("Timestamp\t\tSensor Data")
        print("-" * 40)
        for timestamp, value in data:
            print(f"{timestamp}\t{value:.2f}")

    # complete this function to find the max, min , average of the red data
    def display_analytics(self, analytics):
        if analytics:
            average, minimum, maximum = analytics
            print("Analytics Results")
            print("-" * 40)
            print(f"Average: {average:.2f}")
            print(f"Minimum: {minimum}")
            print(f"Maximum: {maximum}") 


## Bonos!
# you can also generate some figures using the data and python modules like matplotlib, etc
# if simple GUI can be used. Hint: you can use django
# any extra flavor that you think it can add to the task. Hint(use your imagination and skills)
