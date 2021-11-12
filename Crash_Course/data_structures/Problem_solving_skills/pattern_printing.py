# print pattern like this:
"""
#*
**
***
****
"""
class PatternPrinting():
    """ Prints pattern in certain order."""

    def __init__(self, number):
        """ get the user's number for pattern printing. """
        self.number = number

    def print_pattern(self):
        for i in range(1, 2):
            for j in range(1, self.number + 1):
                print('*' * j) 

obj1 = PatternPrinting(5)
output1 = obj1.print_pattern()
print(output1)
        
