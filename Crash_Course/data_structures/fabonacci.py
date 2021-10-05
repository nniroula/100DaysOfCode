class FabonacciNumber():
    """ This class defines fabonacci number pattern. Fibanacci is a number pattern in which each number is a sum of
    preceeding two numbers. Fabonacci number starts at 0 and 1. """

    def __init__(self, num):
        """ It defines a fabonacci number pattern and num is the number upto which a fabonacci pattern will be 
        generated. """
        self.num = num

    def fabonacci_pattern(self):

        initial_fab = [0, 1]
        if self.num > 2:
            count = 2
            while count < self.num:
                # for val in initial_fab:
                sum = initial_fab[-2] + initial_fab[-1]
                initial_fab.append(sum)
                count += 1
        return initial_fab

obj = FabonacciNumber(5)
fab_pattern = obj.fabonacci_pattern()
print(fab_pattern)




