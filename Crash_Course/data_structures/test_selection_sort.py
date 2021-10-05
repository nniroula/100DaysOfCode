from selection_sort import SelectionSort
import unittest

class TestSelectionSort(unittest.TestCase):
    def setUp(self):
        list1 = [3, 7, 2, 5, 1, 4, 6]
        self.object1 = SelectionSort(list1)

    def test_selection_sort(self):
        """ To test the selection method."""
        get_sorted = self.object1.selection_sort()
        self.assertEqual(get_sorted, [1, 2, 3, 4, 5, 6, 7])
        
unittest.main()


