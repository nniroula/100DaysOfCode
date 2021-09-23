# explains about inheritance

class Car():
    """ Simple example to define a class and also inheritance. """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.price = 0

    def set_price(self, price):
        self.price = price
        return self.price

car = Car("CRV", "Honda", 2021)
# print(car.make)
# print(car.model)
# print(f"The year of manufacturing is {car.year}.")
car.set_price(35000)
# print(car.price)

# Inheritance

class ElectricCar(Car):
    """ This is a child class. We are doing inheritance example here. """
    def __init__(self, make, model, year, condition):
        # call parent's constructor
        super().__init__(make, model, year)
        self.condition = condition

    def describe_car(self):
        return f"The instance of an electric car is as follows: \n\t{self.make} {self.model} {self.year} {self.condition}"

ecar = ElectricCar("Chevy", "Traverse", "21", "very good condition")
# print(f"The make of an electric car is {ecar.make}.")
call_method = ecar.describe_car()
print(call_method)
