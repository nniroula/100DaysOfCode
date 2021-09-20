
def get_name():
    """ this function gets a user name and displays it. """
    name = input("Enter your name: ")
    print(f"Hello, {name.title()}!")
    # this does not simply display anything if you do not call this function.
# function call
#get_name()

# postional argument - order in which you pass argument matters.
def add(x, y):
    """ Adds two numbers. """
    return x + y
    # go to ipyhon, do %run func.py, and then do add(2, 3)

# keyword arguments is a argument-value pair that you pass in when you call a function.

def name_work(name, work):
    """ uses keyword arguments pair for passing arguments. """
    return f"Hello {name}, I like {work}."

# print(name_work(name = "Nabin", work = "Student"))
# print(name_work(work = "Software Engineering", name = "Nbain"))
name_work(work = "Customer Service", name = "Nabin")


# Default values in functions

def default_values(name, work = "Software Engineering"): # this is called a default value, could be overridden in func call
    """ uses default parameter values. """
    return name + ", " + work
# ways to call this function. 
#1 withour overriding any values
no_overriding = default_values("Nabin")
print(f"Output before overriding the default parameter is {no_overriding}")

with_overriding = default_values(name = "NK", work = "Student")
print(f"Output after overring the default parameter is {with_overriding}")

