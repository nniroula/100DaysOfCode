import unittest
from binary_search import BinarySearch

class TestBinarySearch(unittest.TestCase):
    """ tests BinarySearch class. """

    def test_binary_search_list(self):
        list1 = [2, 4, 6, 8, 12, 14]
        obj1 = BinarySearch(list1, 14)
        result1 = obj1.binary_search()
        self.assertEqual(True, result1)  # this function is called one test no matter how many assert statements you have in it.
        self.assertFalse(False, result1)

unittest.main()