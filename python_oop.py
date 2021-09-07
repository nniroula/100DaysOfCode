#!/Users/nabinniroula/anaconda3/bin/python

""" Classic example of python OOP Concept. """

# To check the type of data type
x = 1
# print(type(x))
# print(type("hello"))

class Dog:
    # constructor for Dog class
    def __init__(self):
        print("This is __init__ method. ")
        self.bark()
        self.legs()
    def bark(self):
        print("bark")
    
    def legs(self):
        print("It has four legs")
d1 = Dog()
# print(d1.bark())
# print(d1.legs())
# print(type(d1))