import unittest,csv
from Railroad import *

class TestRailRoads(unittest.TestCase):

    def setUp(self):
        self.csv_file = open("testinput.csv")
        self.read_file = csv.reader(self.csv_file)
        departure,arrival,cities,result=Roads.readRailInfo("testinput.csv")
        self.city=cities
        self.start_station=departure
        self.end_station=arrival

    def test_Fileinfo(self):
        departure,arrival,cities,result=Roads.readRailInfo("testinput.csv")
        self.assertTrue(result)

    def test_cities(self):
        test_city=['madurai', 'chennai', 'tambaram', 'vilupuram', 'kovai', 'dindugal', 'tiruchy']
        departure,arrival,cities,result=Roads.readRailInfo("testinput.csv")
        self.assertEqual =(cities,test_city) 

    def test_NotListCities(self):
        test_city=['tambaram', 'vilupuram', 'kovai', 'dindugal']
        departure,arrival,cities,result=Roads.readRailInfo("testinput.csv")
        self.city=cities
        self.assertNotEqual =(cities,test_city)

    def test_PassengerInfo(self):
        list_city=self.city
        Result,SuccessResult=Roads.getPassengerInfo(list_city,True)
        self.assertTrue(SuccessResult)
      
if __name__ == '__main__':

    Roads = Railroads()
    unittest.main()

