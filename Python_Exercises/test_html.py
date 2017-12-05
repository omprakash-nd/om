import unittest
from HtmlTagDetect import HTMLParser

class TestHtmlTags(unittest.TestCase):

    def setUp(self):
        self.html_file = open("test_input.txt")
        self.read_file = self.html_file.read()
        
    def test_fileName(self):
        result = html.check_fileformat('test_input.txt')[0]
        self.assertEqual(result, 'test_input.txt')
        self.assertNotEqual(result, 'test_input')


    def test_fileReturnTags(self):
        test_open = html.open_file('test_input.txt',True)[0]
        self.assertIn(test_open, self.read_file) 

    def test_fileAttributes(self):
        return_value = html.check_fileAttributes(self.read_file,True)[0]
        self.assertEqual(return_value, ['head', 'title', 'object', 'param']) 
   
if __name__ == '__main__':
    html = HTMLParser()
    unittest.main()













