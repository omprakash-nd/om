import unittest
import csv
from Railroad import *

class TestRailRoads(unittest.TestCase):
    def setUp(self):
        self.csv_file = open("testinput.csv")
        self.read_file = csv.reader(self.csv_file)
        departure, arrival, cities, result = Roads.readRailInfo("testinput.csv")
        self.city = cities
        self.start_station = departure
        self.end_station = arrival

    def test_file(self):
        result = Roads.readRailInfo("testinput.csv")
        self.assertTrue(result)

    def test_file(self):
        result = Roads.readRailInfo("testinput.txt")
        self.assertTrue(result)

    def test_passenger(self):
        list_city = self.city
        passenger=['tambaram', 'vilupuram',1200]
        start = passenger[0]
        end = passenger[1]
        Result, SuccessResult = Roads.checkPassenger(list_city, passenger, True)
        self.assertIn(end, list_city)

    def test_wrong_stations(self):
        list_city = self.city
        passenger = ['tambaram', '', 1200]
        end = passenger[1]
        Roads.checkPassenger(list_city, passenger, True)
        self.assertNotEqual(end, list_city)

    def test_wrong_time(self):
        list_city = self.city
        passenger=['tambaram', 'chennai', 26345]
        time = passenger[2]
        Roads.checkPassenger(list_city, passenger, True)
        self.assertNotEqual(time, list_city)
    
if __name__ == '__main__':
    Roads = Railroads()
    unittest.main()
