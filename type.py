#!/Users/nabinniroula/anaconda3/bin/python

""" Here, we will deal with the type() function in Python. """

print(type(3))
print(f"the type is as follows: {type('Nabin')}")
print(type(12.34))

# class type with type function
class Test:
    s = 'testing'
t = Test()
print(type(t))
