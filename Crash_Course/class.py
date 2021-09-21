class Restaurant():
    def __init__(self, restuarant_name, cuisine_type):
        self.restaurant_name = restuarant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        # if self.restaurant_name:
        #     return self.restaurant_name
        # if self.cuisine_type:
        #     return self.cuisine_type
        # print(self.restaurant_name)
        # print(self.cuisine_type)
        return f"{self.restaurant_name} \n{self.cuisine_type}"

    def open_restaurant(self):
        return "The restaurant is open."

# instance of the class
restaurant = Restaurant("Nabin's Cafe", "Remix")
# print(restaurant.restaurant_name)
# print(restaurant.cuisine_type)

describ = restaurant.describe_restaurant()
print(describ)

open_res = restaurant.open_restaurant()
print(open_res)