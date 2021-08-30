#!/Users/nabinniroula/anaconda3/bin/python

""" This is for a lambda function - whihc is used to create anonymous functions. lambda keyword is like def in func definition"""
sum = lambda a, b: a + b
#print(f"The sum is {sum(2, 4)}.")

string = "Lambda function here"
#print(lambda string: print(string))

# lambda function in filter() function
sequences = [10, 2, 8, 7, 5, 4, 3, 11, 0, 1]
filtered_result = filter(lambda x: x>4, sequences)
#print(filtered_result)  # this returns function object
print(list(filtered_result))

# eg 2
arr = [1, 2, 3, 4, 5, 6]
filtered_evenList = filter(lambda a: a%2 == 0, arr)
print(f"filtered even list is {list(filtered_evenList)}.")

# lambda function as a parameter in map()
sequence = [2, 4, 6, 8]
filtered_ans = map(lambda x: x*x, sequence) # this returns function object, convert it to list with list()
print(f"The output of the map function after lambda() is passed as an arguemnt {list(filtered_ans)}.")

# eg 2
arr = [1, 2, 3, 4, 5, 6]
reminder = map(lambda a: a%2, arr)
print(f"The reminder list is {list(reminder)}.")



