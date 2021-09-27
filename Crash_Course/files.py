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
"""
# store a file in a variable and access it in the for loop
file_to_read = "names.txt"
print(f"File before for loop is {file_to_read}")
print("reading file ................. ")
with open(file_to_read) as file_to_be_read:  # reads file and stores file object in file_to_be_read
    for line in file_to_be_read:
        print(line.rstrip()) # end of the line adds blank line at the end, and also print() adds another blank line.
                            # rstrip() removes those 2 blank lines

