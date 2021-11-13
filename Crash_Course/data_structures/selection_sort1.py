class SelectionSort1():
    """ this deals with selection sort algorithm. """

    def __init__(self, list1):
        """ Get the list. """
        self.list1 = list1

    def selection_sort(self):
        """ defines the selection sort concept. """
        #pass
        for i in range(len(self.list1) - 1):  # this loop is for number of iterations(passes)
            # find the minimum value
            minimum_value_index = i 
            # get another loop for finding miimum value
            # for j in range(1, len(self.list1)):  
            for j in range(i, len(self.list1)):    # do not start at 1, start at i
                if self.list1[minimum_value_index] > self.list1[j]:
                    temp = self.list1[minimum_value_index]
                    self.list1[minimum_value_index] = self.list1[j]
                    self.list1[j] = temp 
        return self.list1

# list1 = [7, 4, 10, 8, 3, 1]
# obj1 = SelectionSort1(list1)
# output = obj1.selection_sort()
# print(output)

# list2 = [8, 10, 4, 2, 6]
# obj2 = SelectionSort1(list2)
# output2 = obj2.selection_sort()
# print(output2)

