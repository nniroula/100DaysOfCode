#!/Users/nabinniroula/anaconda3/bin/python

""" Classic example of python OOP Concept. """

"""
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

"""
# eg 3 student and course classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 1 - 100 numeric values only

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name_of_course, max_std):
        self.name_of_course = name_of_course
        self.max_std = max_std
        self.enrolled_std = []
    
    def add_std(self, student):
        if len(self.enrolled_std) < self.max_std:
            self.enrolled_std.append(student)
            return True
        else:
            return False

    def get_std(self):
        # return [std for std in self.enrolled_std]
        for std in self.enrolled_std:
            return std

student1 = Student("Nabin", 34, 90)
student2 = Student("Prabha", 1, 100)

# add student to the course, add student1 and student2 to the course
course1 = Course("Computer Science", 2)
course1.add_std(student1)

print(course1.add_std(student1))
# print(course1.enrolled_std)
print(course1.get_std())


