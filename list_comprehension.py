#!/Users/nabinniroula/anaconda3/bin/python

""" This talks about comprehension, and especially list comprehension. """

# Traditional approach(very standard approach)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# get an even list from this list
even_list = []
for i in list1:
    if i%2 == 0:
        even_list.append(i)

# print(even_list)

# List comprehension way
evens = [i for i in list1 if i%2 == 0]
print(evens)