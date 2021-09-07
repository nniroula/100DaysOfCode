#!/Users/nabinniroula/anaconda3/bin/python

""" Classic example of python OOP Concept. """

# To check the type of data type
x = 1
# print(type(x))
# print(type("hello"))

# eg 1

class Dog:
    # constructor for Dog class
    def __init__(self):
        print("This is __init__ method. ")
        self.bark()
        self.legs()

    def bark(self):
        return "bark"
    
    def legs(self):
        return "It has four legs"
d1 = Dog()
# print(d1.bark())
# print(d1.legs())
# print(type(d1))

# eg 2

class Dog1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

dog1 = Dog1("Tim", 6)
print(f"It's name is {dog1.name}.")

dog2 = Dog1("John", 24)
print(dog2.name)
print(f"The age of {dog2.name} is {dog2.age}.")

# second way of assigning a value to an objct is as follows
dog1.name = "Sakira"
print(f"The updated name of the dog 1 object is {dog1.name}.")

# If there are thousands of objects, the above idea of setting and getting object attributes do not work. So, use get and set methods

# eg 2
class Dog2:
    def __init__(self):
        # self.name = name
        # self.age = age
        # if it says that name is not defined, set it to "None"  for initialization
        # self.name = "None" # Or set it to empty string
        self.name = " "
        # self.age = "None" # Or set it to 0
        self.age = 0

    def set_name(self, new_name):
        self.name = new_name
    
    def set_age(self, age):
        self.age = age
    
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

dog_1 = Dog2()
dog_1.set_name("Eunta")
dog_1.set_age(10)
print(f"The name of the dog 1 object using set() is {dog_1.get_name()}.")
print(f"The age of the dog object using set and get method is {dog_1.get_age()}.")

