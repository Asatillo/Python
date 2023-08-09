import statistics

class DataProcessor:
   
    @staticmethod 
    def calculate_average(data):
        av = statistics.mean([value for _, value in data])
        return av
        

    @staticmethod
    def calculate_min(data):
        return min(data)

    @staticmethod
    def calculate_max(data):
        return max(data)