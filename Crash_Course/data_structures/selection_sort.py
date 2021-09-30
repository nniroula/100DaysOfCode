class SelectionSort():
    """ Here we will deal with selection sort. find the minimum element of the unsorted region and move it to the front
    until all the elements are sorted in the similar approach. """
    def __init__(self, array):
        self.array = array

    def selection_sort(self):
        """ selection sorts a given list."""
        list1 = []
        while len(self.array) > 0:
            min_val = min(self.array)
            self.array.remove(min_val)
            list1.append(min_val)

        return list1

list1 = [4, 9, 6, 5, 2, 1]
selection_sort = SelectionSort(list1)
print(selection_sort.selection_sort())

# have same element twice
