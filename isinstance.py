#!/Users/nabinniroula/anaconda3/bin/python

""" This deals with an isinstance method in python. It takes 2 arguments to check if 1st argument is an instance of 2nd. """
age = isinstance(34, int)
print(age)

num = isinstance(3.142, int)
print(num)

name = "Nabin"
print(f"should return True for string, {isinstance(name, str)}.")

# class for isinstance(), create an object and compare that object to that class
class MyName:
    name = 'Nabin'
# create an object
myClass = MyName()
instance_check = isinstance(myClass, MyName)
print(f"should return true becuase myClass is an instance of the class MyName: {instance_check}.")