import unittest
from Problem1 import CheckHTML

class TestHtmlTags(unittest.TestCase):

    def setUp(self):
        self.html_file = open("sample.txt")
        self.read_file = self.html_file.read()
        
    def test_fileName(self):
        result = html.check_fileformat('sample.txt')[0]
        self.assertEqual(result, 'sample.txt')
        self.assertNotEqual(result, 'sample')


    def test_fileReturnTags(self):
        test_open = html.open_file('sample.txt',True)[0]
        self.assertIn(test_open, self.read_file) 

    def test_fileAttributes(self):
        return_value = html.check_fileAttributes(self.read_file,True)[0]
        self.assertEqual(return_value, ['head', 'title', 'object', 'param'])
   
if __name__ == '__main__':
    html = CheckHTML()
    unittest.main()













