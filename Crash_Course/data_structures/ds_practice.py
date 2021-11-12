class LinearSearch():
    """ This class for coding data structures review only. """
    # linear search
    #arr = [2, 4, 6, 8]
    # search 6

    def __init__(self, list1, num):
        self.list1 = list1
        self.num = num
    
    def linear_search(self):
        """ uses linear searach algorithm. """
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
