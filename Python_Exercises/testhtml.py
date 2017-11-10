import unittest
from Problem1 import *

class TestHtmlTags(unittest.TestCase):
    obj = CheckHTML()
    fname = 'sample.txt'
    test_fn = obj.get_FileName(fname)
    print obj.get_FileName(fname)

    def test_upper(self):
        self.assertEqual(test_fn,"sample.txt")
if __name__ == '__main__':
    unittest.main()
