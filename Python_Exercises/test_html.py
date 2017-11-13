import unittest
from Problem1 import CheckHTML

class TestHtmlTags(unittest.TestCase):
    def test_filename(self):
        
        result=html.get_FileName('sample.txt')
        self.assertEqual(result, 'sample.txt')
        self.assertNotEqual(result, 'sample')

    def test_tags(self):
        result = html.check_Attributes()
        expectedresult=(['head', 'title', 'object', 'param'])
        self.assertEqual(result, expectedresult)
        self.assertNotEqual(result,"['head','object', 'param']")

    def test_choice(self):
        result = html.display()
        print result
        self.assertEqual(result,False)
        
if __name__ == '__main__':
    
    html = CheckHTML()
    unittest.main()
