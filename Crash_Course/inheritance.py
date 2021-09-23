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
print(car.make)
print(car.model)
print(f"The year of manufacturing is {car.year}.")