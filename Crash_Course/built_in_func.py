name = "Nabin Niroula"
my_name = name.title() # title() converts the first letter of the each word to upper case.
# print(f"This is due to title() function: {my_name}.")

#print(f"this is due to lowr() function in python, {name.lower()}.")
#print(f"This is due to upper() funciton in pythonn, {name.upper()}.")

# new lines and tabs in python - \n and \t

new_lines_and_tabs = ("Languages are: \n\tPython\n\tJavascript\n\tHTML\n\tCSS\n\tSQL")
#print(new_lines_and_tabs)

""" striping white spaces in strings. White spaces include tabs, spaces, and newline characters. """

#1 remove white spaces to the right with rstrip() function
college3 = "Univerisyt of Colorado, Denver "
remove_space = college3.rstrip()
#print(remove_space)

# 2 remove space at the beginning of the string with lstrip() method
college2 = " MSU Denver."
remove_left_space = college2.lstrip()
#print(f"After the space is removed, {remove_left_space}")

#3 remove spaces on both sides using strip() method
developer_school = " Springboard "
remove_space_both_side = developer_school.strip()
#print(f"After the space is removed on both sides, {developer_school}.")

# does strip() has side effect if used ot remove only left or right end space
college1 = " Comminity Colelge of Aurora"
#print("Afer space at beginning is removed is" + college1.strip())
#print("The space after ',' is not due to strip() method to removoe space, " + college1.strip())

#1 personal message
name = "Pabha Niroula" # in titlecase, lowercase, and uppercase
# print(f"Hello {name.title()}, welcome to Python programming. ")
# print(name.lower())
# print(name.upper())

#2 striping white spaces like spaces, tabs, and newline characters with lstirp(), rstrip(), and strip() methods

name1 = "\n\tPabira Niroula\n Nabisha Niroula \tPrinsu Niroula"
# name2 = "Prinsu Niroula"
# Now remove all the white spaces
# print(f"Before white spaces are removed: {name1}")
# print(f"After white spaces are removed: {name1.strip()}") # only removes white spaces from the beggin and the end, not from the middle

# print number 8 using +, -, *, /, //, %, **
plus_ans = 6 + 2
minus_ans = 10 - 2
divide_ans_one_slash = 16/2
divide_ans_two_slash = 16//2
multiply_ans = 4 * 2
exponent_ans = 2**3
modulo_ans = 18 % 10

# use \ to break a line into multiple lines
#print(f"\tAfter Plus operation: {plus_ans}\n\tAfter minus operation is {minus_ans}\n\tAfter One Slash operation is \
#{divide_ans_one_slash}\n\tAfter Two Slash operation is {divide_ans_two_slash}")

""" Lists """
#1 append() to add an element to the end of the list
#2 insert(index_where_you_want_to_put_item, item_name)
list1 = ["Nabin", "pabi", "prinshu"]   # This lets you insert anywhere in the list and shifts other elements accordingly
list1.insert(1, "Nabisha")
# print(list1)

#3 use the del statement to list an item from a list you know the index of an item
del list1[0] # removes the first item.

#4 pop() or pop(index_of_item)
list1.pop() # removes the last item from the list, but we can store this value in a variable and use it againf. This
# is not possible with the del statement-once you use del, you remove it permanently.

#5 remove() method - use it if do not know an index of an item you want to remove
#list1.remove('Item_you_want_to_remove')

# To print a string as it is or in the raw form, use print(r'content may conatin \n or \t like pythonic things')
#print(r'\n Nabin Niroula \t')  # displays \n Nabin Niroula \t

invitees = ["nabin", "pabitra", "Prinsu"]
# for person in invitees:
#     print(f"Hello {person}, You are invited to the party")

#print(f"{invitees[0]} cannot make to the party")

# To add new person in that place you can do the following
invitees[0] = "Jemie" # or 
invitees.insert(0, "Jemie") # or

# To remove that person
invitees.remove('pabitra')
#print(invitees.remove('pabitra')) # you do not get anything back because remove removes it completely and no return value.

# To sort, and reverse the list
list2 = ["CU", "Metro", "ACC"]
# print(list2)
# reversed_order = list2.reverse()
# print(reversed_order) , # you have to reverse the list and then print it.
list2.reverse()
# print(list2)

# use sort() method to sort in alphabetical order, but also that list is reverse
list2.sort(reverse=True)
#print(list2)

""" List comprehension """
# numbers = [1, 2, 3, 4, 5, 6]
# for num in range(1, 10): # 1o is excluded
#     print(num)

# for the same for loop above, put the result in list
list_num = []
for num in range(1, 10): # 1o is excluded
    list_num.append(num)
    # print(num)
#print(list_num)

# now use list comprehension
list_comprehension = [num**2 for num in range(1, 9)]
# print(f"After list comprehension: {list_comprehension}")

million = [num for num in range(1, 1000000)]
# print(million)
max_val = max(million)
# print(f"Maximum value in a list is {max_val}")

min_val = min(million)
# print(f"Minimum value in a list is {min_val}")

sum_list = sum(million)
# print(f"The sum of the vlaues in the list is {sum_list}")

# list comprehension for the odd numbers
odd_list = [odd for odd in range(1, 20, 2)]
# print(odd_list)

even_list = [num for num in range(1, 20) if num % 2 == 0]
# print(f"Even list is:\n\t {even_list}")

# list slicing and copying
languages = ["HTML", "CSS", "JS", "Python"]
copy_of_lang = languages[:]
#print(languages)

lang1 = ["Js", "Python", "Java", "C++"]
lang2 = lang1 # this means lang2 points to the lang1. Any changes made to one of them will have affect on others. This is different than coping with [:]
# print(f"lang1 is {lang1}")
# print(f"lang2 is {lang2}")
lang2.append("Scala")
# print(f"lang2 after appending an element is {lang2}")
# print(f"lang1 should also be same as the lang2, {lang1}")

# tuple = immutable list
foods= ("Rice", "Taco", "nuggets", "sandwich", "burrito")
# print(f"The food tuple is {foods}")
first_item = foods[0]
# print(first_item)

# for food in foods:
#     print(food)

#list enhancement
list_enh = [food for food in foods]
# print(list_enh)

# try to change the first item in a tuple and see what happens
#foods[0] = "banana"  # TypeError: 'tuple' object does not support item assignment

# "in" operator to check membership in a list
ages = [12, 24, 45, 36]
# if 24 in ages:
#     print(True)

# print(36 in ages)
# print(10 in ages) # should return False

# 'not in' operator
not_in = 13 not in ages # should return True
# print(not_in) 

""" an empty list evaluates to False """
schools = [] # empty list
if schools:  # this evaluates to False b/c if schools: means if there is at least one item in that list, False otherwise
    # print("It's a nice school.")      # in list: case, Python evaluates to True or False
    "Nice"
"""
five_users = ["admin", "charles", "john", "alex", "hether hut"]

if five_users: # this means if the list is not empty
    for user in five_users:
        if user.lower() == "admin":
            print(f"Hello {user.title()}, You are at a great position.")
        if user.lower() != "admin":
            print(f"Hello {user.title()}, You are awesome.")
else:
    print("We need to get some users.")
"""

"""
current_users = ["bob", "daniel", "mark", "kevin", "katie"]
new_users = ["Katie", "Mark", "Novice", "Code newbie"]

# check if the user name has already been use-make case insensitive to check
if current_users and new_users: # to make sure that lists are not empty
    for new_user in new_users:
        if ((new_user.lower() in current_users) or (new_user.title() in current_users)):
            print("User name is in use, create a different user name.")
        else:
            print("User name is accepted!")
else:
    print("It looks like a list or both might be empty.")

"""
# Ordinal numbers - 1st, 2nd, 3rd and so forth
for num in range(1, 7):
    if num == 1:
        print("1st")
    elif num == 2:
        print("2nd")
    elif num == 3:
        print("3rd")
    elif num == 4:
        print("4th")
    elif num == 5:
        print("5th")
    else:
        print("6th")







