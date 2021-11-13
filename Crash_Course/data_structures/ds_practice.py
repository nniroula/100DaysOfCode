"""
class LinearSearch():
    # linear search
    #arr = [2, 4, 6, 8]
    # search 6

    def __init__(self, list1, num):
        self.list1 = list1
        self.num = num
    
    def linear_search(self):
        for i in range(len(self.list1)):
            if self.list1[i] == self.num:
                print("at index: ", i)
                return "Found"
        return "Number not found"

# create object here
arr = [2, 4, 6, 8]
linearsearch = LinearSearch(arr, 8)
result1 = linearsearch.linear_search()
print(result1)

"""

# binary search algo
  #arr = [2, 4, 6, 8], search 4.

"""
class BinarySearch():

    def __init__(self, list1, num):
        self.list1 = list1
        self.num = num
        self.starting_index = 0
        self.ending_index = len(self.list1) - 1
        self.list1.sort()
    
    def binary_search(self):
        found = False
        while not found and self.starting_index <= self.ending_index:
            mid_point = (self.starting_index + self.ending_index)//2
            if self.num == self.list1[mid_point]:
                found = True
            else:
                if self.num > self.list1[mid_point]:
                    self.starting_index = mid_point + 1
                    # continue
                if self.num < self.list1[mid_point]:
                    self.ending_index = mid_point - 1
                    # continue
        return found

arr = [2, 4, 6, 8]
obj1 = BinarySearch(arr, 8)
output1 = obj1.binary_search()
print(output1)


"""


"""
# sorting algorithms 
#1 bubble sort
# [2, 3, 1, 6, 4, 5, 9, 8]

class BubbleSort():
    def __init__(self, arr):
        self.arr = arr

    def bubble_sort(self):
        for j in range(len(self.arr) - 1):
        # for j in range(1):
            for i in range(len(self.arr) - 1 - j):
                if (self.arr[i] > self.arr[i + 1]):
                    temp = self.arr[i]
                    self.arr[i] = self.arr[i + 1]
                    self.arr[i + 1] = temp
        return self.arr

# object
arr1 = [2, 3, 1, 6, 4, 5, 9, 8]
obj1 = BubbleSort(arr1)
output1 = obj1.bubble_sort()
print(output1)

"""

# insertion sort
# divide a list into sorted and unsorted sublist. First element is a sorted list and rest is unsoted sublist.
# we will need two loops- outer loop- it counts from first element in the list to the end of the list
# inner loop, it decrements from the index of last sorted element to zero

class InsertionSort():

    def __init__(self, arr):
        self.arr = arr 

    def insertion_sort(self):
        for i in range(1, len(self.arr)): # goes up to 1 less than the length of an array
            j = i - 1
            current_value = self.arr[i]  # temp value
            while current_value < self.arr[j] and j>= 0:
                self.arr[j + 1] = self.arr[j]
                j = j - 1
            self.arr[j + 1] = current_value
        return self.arr

# instantiate the class
arr = [5, 4, 10, 1, 6, 2]
obj1 = InsertionSort(arr)
result1 = obj1.insertion_sort()
print(result1)
