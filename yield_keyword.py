#!/Users/nabinniroula/anaconda3/bin/python
""" Here, we will learn about yield keyword in python that returns generator object. """

#eg 1
def testyield():
    yield "Welcome to python learning."
output = testyield()
# print(output)

# print("After Iterating through the generator object, we get: ")
for i in output:
    print(i)

def return_square(n):
    """ This function returns the square of a number."""
    return n*n

def get_square(n):
    for i in range(n):
        yield return_square(i)

    # yield returns generator object, to get the actual values- use for loop or list or next method
square = get_square(10)
#print(square) # prints geneartor object
# for i in square:
#     print(i)

# second way is 
print(list(square))

# Third way is
print(next(square))   # error message with next() method means that there is no more item to iterate through.




