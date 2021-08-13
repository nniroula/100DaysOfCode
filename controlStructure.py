#!//Users/nabinniroula/anaconda3/bin/python

# 1  if, elif, and else statements.
userInput = input("Please enter your favorite number: ")
# since input function returns string, convert it to integer with int function.
x = int(userInput)
if x == 1:
    print("One")
elif x == 2:
    print("Two")
elif x == 3:
    print("Three")
elif x == 4:
    print("Four")
else:
    print("I cannot guess your number. ")

#2 for loop in python
#Q 1 create a list and use for loop to iterate through each element
list1 = ["john", "steve", "jeff", "Jerry", "Eric", "Brad"]
for name in list1:
    print(name) # this prints each element in a list.

#Q 2 Create a program that counts from 0 to 100

# use range(argument) function

for num in range(100):
    print(num)

#Q 3 output 1 to 100 backwards


