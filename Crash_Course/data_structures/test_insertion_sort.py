from insertion_sort import InsertionSort
import unittest

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        # instantiate InsertionSort class
        list_a = [6, 4, 2, 9, 1]
        instance = InsertionSort(list_a)
        result = instance.insertion_sort()
        self.assertEqual([1, 2, 4, 6, 9], result)

unittest.main()