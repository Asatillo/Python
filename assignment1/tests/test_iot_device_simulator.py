import unittest
from datetime import datetime
from sensor import Sensor
from data_processor import DataProcessor
from communication import Communication
from device import Device
from dashboard import Dashboard

class TestIoTDeviceSimulator(unittest.TestCase):
    def setUp(self):
        self.sensor = Sensor(0, 100)
        self.data_processor = DataProcessor()
        self.communication = Communication("https://central-server.example.com")
        self.device = Device(self.sensor, self.data_processor, self.communication)
        self.dashboard = Dashboard()

    def test_sensor_data_range(self):
        for _ in range(1000):
            timestamp, sensor_data = self.sensor.read_data()
            self.assertTrue(isinstance(timestamp, datetime))
            self.assertTrue(0 <= sensor_data <= 100)

    def test_data_processor_average(self):
        data = [(datetime.now(), value) for value in [1, 2, 3, 4, 5]]
        values = [value for _, value in data]
        average = self.data_processor.calculate_average(values)
        self.assertEqual(average, 3)

    def test_data_processor_min(self):
        data = [(datetime.now(), value) for value in [1, 2, 3, 4, 5]]
        values = [value for _, value in data]
        min_value = self.data_processor.calculate_min(values)
        self.assertEqual(min_value, 1)

    def test_data_processor_max(self):
        data = [(datetime.now(), value) for value in [1, 2, 3, 4, 5]]
        values = [value for _, value in data]
        max_value = self.data_processor.calculate_max(values)
        self.assertEqual(max_value, 5)

    def test_device_collect_data_length(self):
        self.device.collect_data(5)
        self.assertEqual(len(self.device.data), 5)

    def test_device_collect_data_range(self):
        self.device.collect_data(1000)
        for _, value in self.device.data:
            self.assertTrue(0 <= value <= 100)

    def test_device_process_data_length(self):
        self.device.collect_data(5)
        processed_data = self.device.process_data()
        self.assertEqual(len(processed_data), 3)

    def test_communication_send_data(self):
        self.communication.send_data("Test data")

    def test_communication_receive_data(self):
        self.communication.receive_data()

    def test_dashboard_display_data(self):
        data = [(datetime.now(), value) for value in [1, 2, 3, 4, 5]]
        self.dashboard.display_data(data)

    def test_dashboard_display_analytics(self):
        analytics = (3, 1, 5)
        self.dashboard.display_analytics(analytics)

if __name__ == "__main__":
    unittest.main()