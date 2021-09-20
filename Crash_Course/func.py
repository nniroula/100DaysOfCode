
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
#1 withour overriding default values
no_overriding = default_values("Nabin")
# print(f"Output before overriding the default parameter is {no_overriding}")

# with overriding default values
with_overriding = default_values(name = "NK", work = "Student")
# print(f"Output after overring the default parameter is {with_overriding}")

# making an argument opitonal in function defination

#def optional_arg(fname, mideel_name = " ", lname): # any parameter that comes after optional paramter is not accessible
def optional_arg(fname, lname, middle_name = " "):
    if middle_name:
        name = fname + " " + middle_name + " " + lname
    else:
        name = fname + " " + lname
    return name

func_call1 = optional_arg("nabin", "Niroula")
# print(func_call1)

func_call2 = optional_arg("Nabin", "Niroula", "Keerun")
# print(func_call2)

func_call3  = optional_arg(fname = "Nk", middle_name = "Bhaie", lname = "Niroula")
# print(func_call3)

# return dictionary in function call
def return_dict(name, job):
    """ return dictionary in func call. """
    dict1 = {}
    dict1[name] = job
    return dict1
dict_obj = return_dict("Nbain", "Niroula")
# print(dict_obj)

def pass_list(names):
    """ This passes a lsit as an argument, names works as a list. """
    input_names = [name for name in names]
    return input_names
get_list = pass_list(["John", "dixie", "Henry", "Uhul"])
# print(get_list)
