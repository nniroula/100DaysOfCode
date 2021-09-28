# make a text file callled names.txt and open it, read it, and close it.

"""
f = open("names.txt")
get_names = f.read()
f.close()
# print(get_names)  # this technique adds white space at the end of the output file. to avoid it, use rstrip()

# this method above for reading file may give problem when we are not sure when to close the file. To avoid that 
# problem use "with" keyword as follows.
with open("names.txt") as my_file:
    file_read = my_file.read().rstrip() # use rstrip() to trim white space that gets displayed as a blank line in output
    print(file_read)


# for loop to access each line in a file, store a file in a variable and use that varible 
with open("names.txt") as file_line_read:
    file_lines = file_line_read.read()
    for line in "names.txt":   # this does not work because Python considers names.txt as a stirng than a file
        print(line)

# store a file in a variable and access it in the for loop
file_to_read = "names.txt"
print(f"File before for loop is {file_to_read}")
print("reading file ................. ")
with open(file_to_read) as file_to_be_read:  # reads file and stores file object in file_to_be_read
    for line in file_to_be_read:
        print(line.rstrip()) # end of the line adds blank line at the end, and also print() adds another blank line.
                            # rstrip() removes those 2 blank lines

# readlines() stores output in the form of the list.
read_file = "names.txt"
print("Using readlines() method. ")
with open(read_file) as file_read:
    output = file_read.readlines()  # this holds a list that includes a new line character too for line ending character.
    # print(output)
    # we can use output, which is a list, outside of the with indentation too
for line in output:
    line = line.rstrip()
    print(line)


# Writing single line to a file. 'w' removes the content of the file if the file already exists, and writes new
#content to it, so, be careful while using write to a file

# createa file named programming.txt
file_to_write = "programming.txt"
# with open(file_to_write) as write_content_to_this_file:
with open(file_to_write, 'w') as write_content_to_this_file:   # with 'w', there is no terminal output, you can open the file in finder
    write_content_to_this_file.write("I love programming.")
# Since writing to a file has no terminal output, we would have to read the file's constent and display it
with open('programming.txt') as read_this_file:
    print("After writing to a file: ")
    content = read_this_file.read()  # or read_this_file.readlines()
    print(f"\t{content}")

# append some content to this file
with open(file_to_write, 'a') as appending_something:
    appending_something.write(" Class is a blueprint of objects in OOP concept.\n")
    appending_something.write("Objects are instances of a Class in OOP too.")

with open('programming.txt', 'r') as read_after_append:
    # print("After appending to a file: ")
    # content = read_after_append.read()  # or read_this_file.readlines()
    # print(f"\t{content}")

# you cannot call read() and readlines() within the same "with" key word scope. the seond one will not give an output
    content_readlines = read_after_append.readlines()
    print("After using readlines() function: ")
    for line in content_readlines:
        print(f"\t{line.rstrip()}")
"""

# Q 1 Write a program that prompts the user for the name. When they respond, write their name to a file called guest.txt
user_name = input("Please enter your name: ")
with open("guest.txt", "w") as guest_name:
    guest_name.write(user_name)

# check if the name is wirttent to a file called guest.txt
with open("guest.txt") as file_object:
    print("The file contains the following name(s): ")
    name_in_file = file_object.read()
    print(f"\t{name_in_file}")

# Storing data(such as list) to a file, use json.dump() and json.load()

import json
list1 = [2, 4, 6, 8]  # Store this in a file

file_to_store_data = "list1.txt"
with open(file_to_store_data, "w") as file_object:
    json.dump(list1, file_object)
# print(file_object) prints json object like thing. This means json.dump() has no explicit output. Now read that file 
# to check if list1 is writtent to that file
with open(file_to_store_data) as file_obj:
    numbers = json.load(file_obj)
print(numbers)




