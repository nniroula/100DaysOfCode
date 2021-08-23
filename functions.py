#!/Users/nabinniroula/anaconda3/bin/python

# Functions without parameters:
def name():
    name = input("what is your name? ")
    print(f"Hello, your name is {name}.")
    return f"Thank you {name}."
#print(name())

# Functions with parameters
def add(a, b):
    return a + b
#print(add(2, 3))

# Functions return output in a variable
def outputToVariable(x, y):      # single slash(/) division - returns floating point division value.
    if x == 0:
        return "Operation impossible, zero divisibility problem"
    else:
        return x/y
valueHolder = outputToVariable(6, 2)
#print(valueHolder)

def outputInVariable(x, y):      # double slash(//) division - returns integer division value
    if x == 0:
        return "Operation impossible, zero divisibility problem"
    else:
        return x//y
value = outputInVariable(30, 3)
#print(value)

# make a function that sums the list myList = [1, 2, 3, 4, 5]
def addList(arr):
    sum = 0
    for val in arr:
        sum = val + sum
    return sum
myList = [1, 2, 3, 4, 5]
#print(addList(myList))

# sum is a built in method for list
list2 = [1, 3, 5, 7, 9]
#print(sum(list2))

# min, and max are built in method for list
#print(f"The minimum of list2 is ", min(list2))

#print(f"The maximum value of list2 is ", max(list2))

# To access list items
#print(list2[0])
#print(list2[-1])
print(list2[-3])
list3 = list2[2:4]
print(list3)
