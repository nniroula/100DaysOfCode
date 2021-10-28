import unittest
from sequential_search import SequentialSearch

class TestSequentialSearch(unittest.TestCase):
    """ Tests SequentialSearch """

    def test_sequential_search(self):
        """ test sequential search function """
        #instantiate the class
        list1 = [1, 2, 3, 4]
        inst1 = SequentialSearch(list1, 2)
        result1 = inst1.sequential_search()
        self.assertEqual(True, result1)

    def test_not_in_list(self):
        list1 = [1, 2, 3, 4]
        inst1 = SequentialSearch(list1, 5)
        result1 = inst1.sequential_search()
        self.assertEqual(False, result1)

unittest.main()
        