class SequentialSearch():
    """ This does sequential search """

    def __init__(self, list1, item):
        self.list1 = list1
        self.item = item
        self.found = False

    def sequential_search(self):
        for i in range(0, len(self.list1)):
            if self.list1[i] == self.item:
                self.found = True
            else:
                self.found = False
        return self.found

# instantiate the class
list1 = [1, 2, 3, 4]
inst1 = SequentialSearch(list1, 5)
result1 = inst1.sequential_search()
print(result1)
