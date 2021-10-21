class AddTwoNumbers():
    """ Adds two numbers """
    def __init__(self):
        """ initial the class variables """
        self.num1 = 0
        self.num2 = 0
        # self.get_user_nums()

    def get_sum(self):
        """ get the user input and find the sum"""
        #self.num1 = input("Enter your first number: ")  # this returns string, change it to int
        self.num1 = int(input("Enter your first number: "))
        self.num2 = int(input("Enter your second number: "))
        sum = self.num1 + self.num2
        return sum

# two_nums = AddTwoNumbers()
# in_put = two_nums.get_user_nums()
# print(in_put)
