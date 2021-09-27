# make a text file callled names.txt and open it, read it, and close it.

f = open("names.txt")
get_names = f.read()
f.close()
# print(get_names)  # this technique adds white space at the end of the output file. to avoid it, use rstrip()

# this method above for reading file may give problem when we are not sure when to close the file. To avoid that 
# problem use "with" keyword as follows.
with open("names.txt") as my_file:
    file_read = my_file.read().rstrip() # use rstrip() to trim white space that gets displayed as a blank line in output
    print(file_read)

