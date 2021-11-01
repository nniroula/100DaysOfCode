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
    
    def test_empty_list(self):
        """ tests that a list is empty, returns False. """
        list2 = []
        obj2 = BinarySearch(list2, 5)
        result2 = obj2.binary_search()
        self.assertEqual(False, result2)

    def test_unsorted_list(self):
        """ Tests unsorted list. """
        list3 = [9, 3, 7, 5, 1, 4, 2, 6]
        obj3 = BinarySearch(list3, 7)
        result3 = obj3.binary_search()
        self.assertEqual(True, result3)
        # print(obj3.list)    # to check if a list is sorted.

unittest.main()