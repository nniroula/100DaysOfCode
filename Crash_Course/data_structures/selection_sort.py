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
invoke_func = selection_sort.selection_sort()
print(invoke_func)

# list having same element twice
list2 = [9, 3, 5, 7, 2, 5]
selection_sort2 = SelectionSort(list2)
call_func = selection_sort2.selection_sort()
print(call_func)

# lis have a single element and also an empty list
empty_list = []
selection_emtpy = SelectionSort(empty_list)
call_func_2 = selection_emtpy.selection_sort()
print(call_func_2)

# with one element 
list_one = [10]
select_one = SelectionSort(list_one)
ans = select_one.selection_sort()
print(ans)

# Now write some unit tests for this class.



