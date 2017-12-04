import unittest,csv
from Railroad import *

class TestRailRoads(unittest.TestCase):

    def setUp(self):
        self.csv_file = open("testinput.csv")
        self.read_file = csv.reader(self.csv_file)

    def test_Fileinfo(self):
        departure,arrival,cities,result=Roads.readRailInfo("testinput.csv")
        self.assertTrue(result)

    def test_WrongFileName(self):
        departure,arrival,cities,result=Roads.readRailInfo("testinp.csv")
        print result

        
##    def test_readFile(self):
##        filename =self.csv_file
##        Result = Roads.readFile(filename,True)[3]
##        for data in Result:
##            if data == "['chennai', 'madurai']":
##      self.assertIn(Result,data)
##      
if __name__ == '__main__':

    Roads = Railroads()
    unittest.main()

