class BubbleSort():
    """ this class uses bubble sort algorithm. """

    def __init__(self, list1):
        """ this is a constructor for BubbleSort class. """
        self.list1 = list1

    def bubble_sort(self):
        """ it defines a bubble sort function."""
        for i in range (len(self.list1)):
            if self.list1[i] > self.list1[i + 1]:
                # swap them out
                temp = self.list1[i]
                self.list1[i] = self.list1[i + 1]
                self.list1[i + 1] = temp
        return self.list1

# instantiate the class
arr = [ 2, 8, 6, 4, 5, 3, 7]
obj1 = BubbleSort(arr)
output1 = obj1.bubble_sort()
print(output1)
