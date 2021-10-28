import unittest
from sequential_search import SequentialSearch

class TestSequentialSearch(unittest.TestCase):
    """ Tests SequentialSearch """

    def setUp(self):
        self.list1 = [1, 2, 3, 4]

    def test_sequential_search(self):
        """ test sequential search function """
        #instantiate the class
        inst1 = SequentialSearch(self.list1, 2)
        result1 = inst1.sequential_search()
        self.assertEqual(True, result1)

    def test_not_in_list(self):
        """ test that an item is not in a list """
        inst1 = SequentialSearch(self.list1, 5)
        result1 = inst1.sequential_search()
        self.assertEqual(False, result1)

unittest.main()
        