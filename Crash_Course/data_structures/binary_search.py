class BinarySearch():
    """ uses binary search algorithm. In binary search you always divide list into two halves until you find an item"""

    def __init__(self, list, val):
        """ constructor """
        self.list = list
        self.val = val
        self.list.sort()

    def binary_search(self):
        """ applies binary search algorithm. """
        start_index = 0
        end_index = len(self.list) - 1
        found = False
        while not found  and start_index <= end_index:    # while found != True
            mid_index = (start_index + end_index)//2 
            if self.val > self.list[mid_index]:
                # move start_index to mid_index
                start_index = mid_index + 1
                continue
            if self.val < self.list[mid_index]:
            #     # modve upper bound to mid_index
                end_index = mid_index - 1
                continue
            if self.val == self.list[mid_index]:
                found = True
        return found

# a = [2, 4, 6, 8, 10]
# obj1 = BinarySearch(a, 8)
# output = obj1.binary_search()
# print(output)

