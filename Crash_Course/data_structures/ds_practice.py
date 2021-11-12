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
