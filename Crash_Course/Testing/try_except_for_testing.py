class TryExcept():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def return_quotient(self):
        try:
           result =  self.num2/self.num1
        except:
            return "Zero Divison not allowed."

        else:
            return result

obj1 = TryExcept(0, 2)
print(obj1.return_quotient())


