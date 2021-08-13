#!//Users/nabinniroula/anaconda3/bin/python

#1  Python string replace method
""" The idea is string.replace("Old string", "new String" ) """
name = "Nabin Niroola"
correctName = name.replace("Niroola", "Niroula")
#print(correctName)

#2  python string join(sequence) method
firstName = "Nabinsha"
lastName = "Niroula"
# put them into a sequence
sequence = (firstName, lastName)
# join into new string
name = " ".join(sequence)
#print(name)

#3 find()
name = "my name is not known"
index = name.find("is")
#print(index)

#4 in keyword
name = "first name"
if "first" in name:
    print(f"hello, {name}.")

if "first" in name:
    print(True)
if "ok" not in name:
    print(False)

#5 split() method
""" By default split method uses space as a separator """
college = "Univeristy of Colorado Denver"
w = college.split()
#print(w)

#6 list() method
""" to split words into characters """
word = "University"
splitChar = list(word)
#print(splitChar)

#7 random()
""" To generate random floating point number between 0 and 1, use random module. random is a module, and a module has 
many functions. One of those functions in random moudle is random(). 
"""
#import random module
import random
nums = random.random()
#print(nums)

#8 randrange()
""" generates a random whole numbers between 0 and 10. Takes 2 arguments. """
#import random
val = random.randrange(0, 10)
#print(val)

#9 uniform()
""" To generate random floating point numbers between 1 and 10. Takes 2 arguments. """
# import random
genNum = random.uniform(0, 10)
#print(genNum)

# 10  input() for getting user input
""" iinpt() funtion returns a string, use int() function to convert it to int or whole number. """
num1 = input("Please enter your first number: ")
integer1 = int(num1)
num2 = input("Please enter your second number: ")
integer2 = int(num2)
genrateRandomNum = random.randrange(integer1, integer2)
#print(genrateRandomNum)

# 11 int() function to convert string to int, especially with input() function.
number = input("Enter a number: ")
inInteger = int(number)
print(f"You entered {inInteger}")





