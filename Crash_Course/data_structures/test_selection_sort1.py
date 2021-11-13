import unittest
from selection_sort1 import SelectionSort1

class TestSelectionSort1(unittest.TestCase):
    """ tests SelectionSort1 class """

    def test_selection_sort(self):
        # instantiate the class
        list1 = [7, 4, 10, 8, 3, 1]
        obj1 = SelectionSort1(list1)
        output = obj1.selection_sort()
        self.assertEqual([1, 3, 4, 7, 8, 10], output)

    def test_empty_list(self):
        list2 = []
        obj2 = SelectionSort1(list2)
        output2 = obj2.selection_sort()
        self.assertEqual([], output2)

    def test_one_element_list(self):
        list3 = [1]
        obj3 = SelectionSort1(list3)
        output3 = obj3.selection_sort()
        self.assertEqual([1], output3)

unittest.main()
        
    