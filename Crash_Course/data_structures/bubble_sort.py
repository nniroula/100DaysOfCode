class BubbleSort():
    """ this class uses bubble sort algorithm. """

    def __init__(self, list1):
        """ this is a constructor for BubbleSort class. """
        self.list1 = list1

    def bubble_sort(self):
        """ it defines a bubble sort function."""
        #for i in range(len(self.list1) - 1):
        for i in range(len(self.list1) - 1):
            # for j in range(len(self.list1) - 1):   # this works too
            for j in range(len(self.list1) - 1 - i):  # more efficient approach, in each iteartion comparison reduces by 1
                if (self.list1[j] > self.list1[j + 1]):
                    # swap them out
                    temp = self.list1[j]
                    self.list1[j] = self.list1[j + 1]
                    self.list1[j + 1] = temp
        return self.list1

# instantiate the class
# arr = [2, 8, 6, 4, 5, 3, 7, 22, 14, 18, 12, 20]
arr = ['charles', 'john', 'sarah', 'alex', 'bill']
obj1 = BubbleSort(arr)
output1 = obj1.bubble_sort()
print(output1)
