#!/Users/nabinniroula/anaconda3/bin/python

""" Here we will deal with built in list methods. """
# 1 append() method
list1 = [1]
list1.append(2)
# print(list1)
list1.append(3)
list1.append(4)
#print(list1)

# 2 pop() method
list1.pop()
#print(list1)
list1.pop()
list1.pop()
list1.pop()
#print(list1)

# add items to the list1
list1.append(0)
list1.append(10)
list1.append(20)
list1.append(30)

#print(list1)

# now change the second item in the list
list1[1] = 100
#print(list1)

# 3 sorting a list with sort() method.
list0 = [1, 6, 4, 3, 2, 5]
list0.sort()
#print(list0)

name = ["John", "sam", "Abbie", "Nabisha", "Prinsha"]
name.sort()
#print(name)

# 4 to sort a list in reverse order, reversed() method, you can also reverse using slicing method as in #5
x = [1, 2, 3, 4, 5]
y = list(reversed(x))
#print(y)

# 5 reverse a list using slicing technique
a = [1, 2, 3, 4, 5]
b = a[::-1]   # reversed order is what it gives here
#print(b)

#Q  Given a list with pairs, sort it on the first element, and then sort on the second element.

c = [(3, 6), (4, 7), (5, 9), (8, 4), (3, 1)]
c.sort()
print(c)




