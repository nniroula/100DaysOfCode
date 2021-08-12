#!/Users/nabinniroula/anaconda3/bin/python
def add(a, b):
    """ this function adds two numbers """
    return a + b
print(add(3, 4))

# get user input and use it to do some operations on it
userInputFirst = input("Enter your first name: ")
userInputSecond = input("Enter your last name: ")
firstAndLastName = userInputFirst + ' ' + userInputSecond
print("Your lovely name is " + firstAndLastName + ".")

# use the f string in python, format string (f "....{ } ..")
# Note: f string allows to use varibales inside string.

age = input("Please enter your current age: ")
name = input("please enter your legal name: ")

print(f"Hello {name}, your current age is {age}.")

# write 2 different functions and have second function invoke the first one

def func1():
    """ this function asks user to enter 2 numbers"""
    num1 = input("Enter your first number: ")
    num2 = input("enter your second number: ")
    return num1 * num2

def func2():
    product = func1()
    return product
print("value after 2 func calls is",  func2())

