""" In insetion sort, the first element of the list becomes the sorted list, and remaining elements form
unsorted list. So, start for loop at index 1 and go up to the length of the list."""

class InsertionSort():
    """ This class uses insetion sort. """
    def __init__(self, list1):
        self.list1 = list1

    def insertion_sort(self):
        """ Implement insertion sort. """
        for i in range(1, len(self.list1)):  # first lement, index 0 is sorted list, length contains rest
            # create a temporary variable
            value = self.list1[i]

            j = i - 1

            while j >= 0 and value < self.list1[j]:
                if self.list1[j] > value:
                    # self.list1[i] = self.list1[j]
                    self.list1[j + 1] = self.list1[j]
                    self.list1[j] = value
                j -= 1
        return self.list1

# Driver code:
# a = [6, 4, 2, 9, 1]

# obj = InsertionSort(a)
# print(obj.insertion_sort())







