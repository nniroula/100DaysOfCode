#!/Users/nabinniroula/anaconda3/bin/python
""" In this section we will discuss about inheritance, and implement it in python. """

# Single Inheritance
class Vehicle():
    def __init__(self): #, name, year_made, model):
        self.name = "None"
        #self.name = name
        # self.year_made = year_made
        self.year_made = "None"
        # self.model = model
        self.model = "None"

        self.get_name()
        self.get_model()
        self.get_yearMade()

        self.set_name("set method needs one argument")
        self.set_yearMade("set method needs one argument")
        self.set_model("set method needs one argument")

    def set_name(self, value):
        self.name = value

    def set_yearMade(self, year_manufactured):
        self.year_made = year_manufactured
    
    # def set_model(self, model_of_vehicle):      This does not work b/c self.value has to be self.model from __init__()
    #     self.value = model_of_vehicle
    def set_model(self, model_of_vehicle):
        self.model = model_of_vehicle
    
    def get_name(self):
        return self.name

    def get_model(self):
        return self.model

    def get_yearMade(self):
        return self.year_made
    
vehicle1 = Vehicle()
vehicle2 = Vehicle()

vehicle1.set_name("Truck")
vehicle1.set_yearMade("2000")
vehicle1.set_model("BMW")

vehicle2.set_name("Mini Van")
vehicle2.set_yearMade("2008")
vehicle2.set_model("Highlander")

# print(vehicle1.get_name(), vehicle1.get_model(), vehicle1.get_yearMade())
# print(vehicle2.get_name(), vehicle2.get_model(), vehicle2.get_yearMade())

class Car(Vehicle):
    def __init__(self):
        """ Extra things that this method does. """
        self.wheels = 4
        self.moon_roof = 1

        self.mileage()
    
    def mileage(self):
        return "Gives standard mileage rate on high ways and free ways comparatively. "

car1 = Car()
car2 = Car()

# call the methods from parent class Vehicle
car1.set_name("Honda")
car1.set_model("CRV")
car1.set_yearMade("2021")

car2.set_name("Toyota")
car2.set_model("RAV4")
car2.set_yearMade("2011")

print(car1.get_name(), car1.get_model(), car1.get_yearMade())
print(car2.get_name(), car2.get_model(), car2.get_yearMade())

print(car1.mileage())
print(car2.mileage())

# Third class in this work
class Plane():
    def __init__(self):
        self.wings = 2
        self.wheels = 3
        self.capacity = "None"
        self.crew_members = "None"

        self.set_capacity("definetly")
        self.set_crew_members("sure")

        self.get_capacity()
        self.get_crew_members()

    def set_capacity(self, value):
        self.capacity = value
    
    def set_crew_members(self, value):
        self.crew_members = value
    
    def get_capacity(self):
        return self.capacity

    def get_crew_members(self):
        return self.crew_members

# BEST INHERITANCE EXAMPLE

class A:
    """ contains common functionalities """

    print("THIS IS FROM CLASS A ......................")

    # make class varibales
    input1 = int(input("Please enter your first number: "))
    input2 = int(input("Enter second number: "))

    def __init__(self):
        self.value1 = "None"
        self.value2 = "None"

        self.set_value1()
        self.set_value2()
        self.get_value1()
        self.get_value2()

    def set_value1(self):
        self.value1 = A.input1

    def set_value2(self):
        self.value2 = A.input2
    
    def get_value1(self):
        return self.value1

    def get_value2(self):
        return self.value2
    
# check if class A works as expected

# a = A()
# a.set_value1()
# a.set_value2()
# print(f"The first number is {a.get_value1()}.")
# print(f"The second number is {a.get_value2()}.")

# SINGLE INHERITANCE
class B(A):
    """ Contains add and subtract method method. """

    print("THIS STARTS CLASS B ................ ")

    def __init__(self):
        super().__init__()
        self.add()
        self.subtract()
       
    def add(self):
        # return super().get_value1() + super().get_value2()
        ans = super().get_value1() + super().get_value2()
        return f"The sum is {ans}."

    def subtract(self):
        difference = super().get_value2() - super().get_value1()
        return f"The difference is {difference}."

# Check if class B works as expected 
b = B()
# print(b.add())
# print(b.subtract())

# MULTIPLE INHERITANCE

class C(B):
    """ Inherits from both classes A and B. And also contains divide method. When you inherit from B, and since B inherits 
    from A, you automatically inherit from A. 
    """

    print("CLASS C STARTS HERE..........")
    def __init__(self):
        super().__init__()

        self.multiply()
    
    def multiply(self):
        product = super().get_value1() * super().get_value2()  # these are in class A
        return f"The product is {product}."

# check if class C works properly
c = C()
print(c.multiply())


    


        

