#!/Users/nabinniroula/anaconda3/bin/python

""" Heere we will learn about OOP concepts in python. """

class Dog:
    # name = " "
    # age = 0
    # def bark():
    #     print("bark")
    def __init__(self, legs, tail, age):
        self.legs = legs
        self.tail = tail
        self.age = age
    
# create an object
dog1 = Dog(4, 1, 12)
#print(dog1)

#Q 1 create a Vehicle class with max-speed and mileage instance attribute

class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
# Now, create an Object for the Vehicle class
car = Vehicle(40, 2000)
# print(car)  - this does not work, however, the following works:
# print(car.max_speed)
# print(car.mileage)
# print(car.max_speed, car.mileage)

#Q 2    create a Vehicle class without any variables and methods
# class Vehicle:
#     pass

#Q 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
class Bus(Vehicle):
    pass
bus = Bus(10, 100)
# print(f"The max speed of the bus is {bus.max_speed}.")
# print(f"The milegae of the bus is {bus.mileage}.")

#Q 4    create a Website class that has __init__ and showTitle methods
class Website():
    def __init__(self, title):
        self.title = title

    def showTitle(self):
        return self.title
website = Website("www.learning.org") # website is an object for class Website(class is with capital W)
# print(f"The website after accessing a variable for title is: website.title")
# print(website.showTitle())
# print(f"The website after calling a method to show title is: " + website.showTitle())

# Another example of a class and constructor without anythig as parameters
class Human:
    def __init__(self):
        self.legs = 2
        self.hands = 2
bob = Human()
# print(f"Bob has {bob.legs} legs.")

# Q 5 create a class without any variables and then create some objects. Then define some getter and setter methods 
# to get and set some properties to those objects.

class Friend:
    def __init__(self):
        self.job = "None"
    
    def getJob(self):
        return self.job

    def setJob(self, job):
        self.job  = job
# create obhjects
Alice = Friend()
Bob  = Friend()
# Now set propert job to them
Alice.setJob("Teacher")
Bob.setJob("Professor")
# print those attributes out out
# print(f"The job is {Alice.getJob()}.")
# print(f"The job of Bob is {Bob.getJob()}.")

# Q 6 create a class called car and define some methods in a constructor and mention default behavior in method itself.
class Car:
    def __init__(self):
        self.wheels = 4

        self.drive()
        self.speed()
        self.fuel()

    # now define those methods
    def drive(self):
        return "provides sound driving."
    
    def speed(self):
        return "Gives 32 miles/gallon in free ways and 28 miles/gallon in high ways."
    
    def fuel(self):
        total = 10 
        average = 400//10
        return f"It gives an average of {average} miles per gallon."
    
# create some objects
Honda = Car()
# print(Honda.drive())
# print(Honda.fuel())
# print(Honda.speed())

#Q 7    create a class math that has some methods for calculation for any user input

class Math():
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.add()
        self.subtract()
        self.divide()
        self.multiply()

    def add(self):
        return self.num1 + self.num2
    
    def subtract(self):
        return self.num2 - self.num1

    def divide(self):
        if self.num1 != 0:
            return self.num2//self.num1
        else:
            return "Impossible, Zero divisibility problem."

    def multiply(self):
        return self.num1 * self.num2

# create an object
Add = Math(2, 3)
# print(f"The sum of two numbers is {Add.add()}.")

Subtract = Math(4, 4)
# print(f"The difference of the two numbers is {Subtract.subtract()}.")

Divide = Math(2, 12)
# print(f"The quotient of the two numbers is {Divide.divide()}.")

Multiply = Math(7, 9)
# print(f"The product of the two numbers is {Multiply.multiply()}.")


# Now create a class Job and get all job appications as user inputs

"""
class Job:
    def __init__(self, jobApplication):
        # user inputs
        jobApplication = input("Please enter the recent company that you applied for: ")
        self.jobApplication = jobApplication

        self.getJobApplied()
        self.setJobApplied()

    def getJobApplied(self):
        return self.jobApplication
    
    def setJobApplied(self, job):
        job = input("Please enter the recent company that you applied for: ")
        self.job = job

job = Job()

print(job.getJobApplied())

"""
# create a class computer with some default variable values and later on change those variable values
class Computer:
    def __init__(self):
        self.type = "HP"
        self.CPU = "i5"
    
    def update(self):
        self.type = "Intel"
    
comp1 = Computer()
comp2 = Computer()
# print(f"The brand of object 1 before modification of the value is {comp1.type}.")
comp1.type = "Mac Book Pro"
# print(f"The brand of object 1 after modification is {comp1.type}.")
# print(f"The type for object 2 of Computer class is {comp2.type}.")
# print("\n")
comp1.update()
# print(f"The value after update function is called is {comp1.type}.")

# print("The addresses of the objects are: ")
# print(id(comp1))
# print(id(comp2))

# Compare 2 objects of the same class
class TwoObjectComparision:
    def __init__(self):
        self.name = "object 1"

    def compareTwoObjects(self, secondObject):
        if self.name == secondObject.name:
            return "They are exactly the same objects."
        else:
            return "They are the different objects."
obj1 = TwoObjectComparision()
obj2 = TwoObjectComparision()
obj2.name = "Object 2"
# print(obj2.name)
# print(obj1.compareTwoObjects(obj2))


# Instance vs class variables
class InstanceVsClassVaribales():
    """ static or class varibles are defined in class outside of init method of that class. """
    wheels = 4 # This is a class variable

    def __init__(self):
        """ Variables inside init are called instance variables """
        self.mileage = 10
        self.company = "BMW"
    
object1 = InstanceVsClassVaribales()
object2 = InstanceVsClassVaribales()

# To change the class variable, do className.classVariable = something 
InstanceVsClassVaribales.wheels = 2
#print(f"The modified value for class varibale is now {InstanceVsClassVaribales.wheels}.")

# To access static variables
# print(object1.mileage, object1.company)

# To access class variables
# print(object1.wheels)

# Type of methods in python are Instance methods, static methods, and class methods.
class PythonMethodTypes():
    def __init__(self, score1, score2):
        """ This an example of instance method because it has self key word used. """
        self.score1 = score1
        self.score2 = score2

    def average(self):
        """ This an instance method because it has self key word used in it. """
        return (self.score1 + self.score2)/2

    # instead of doing s1.score1, s2.score2 etc use the following method
    def get_score1(self):
        return s1.score1
    
    def get_score2(self):
        return s2.score2
    
    # instead of doing s1. score1 = something, do the following method setup
    def set_score1(self, value):
        self.value = value
    
    def set_score2(self, value):
        self.value = value


# objects
s1 = PythonMethodTypes(34, 37)
s2 = PythonMethodTypes(13, 23)

print(f"The score1 for s1 obtained using get method is {s1.get_score1()}.")
print(s1.average())

s1.set_score1(10)

print("The score 1 after changing the value of score 1 is {s1.get_score1()}.")















