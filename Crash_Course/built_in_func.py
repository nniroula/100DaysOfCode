name = "Nabin Niroula"
my_name = name.title() # title() converts the first letter of the each word to upper case.
print(f"This is due to title() function: {my_name}.")

#print(f"this is due to lowr() function in python, {name.lower()}.")
#print(f"This is due to upper() funciton in pythonn, {name.upper()}.")

# new lines and tabs in python - \n and \t

new_lines_and_tabs = ("Languages are: \n\tPython\n\tJavascript\n\tHTML\n\tCSS\n\tSQL")
#print(new_lines_and_tabs)

""" striping white spaces in strings. White spaces include tabs, spaces, and newline characters. """

# remove white spaces to the right with rstrip() function
college2 = "Univerisyt of Colorado, Denver "
remove_space = college2.rstrip()
print(remove_space)

# remove space at the beginning of the string with lstrip() method
college1 = " MSU Denver."
remove_left_space = college1.lstrip()
print(f"After the space is removed, {remove_left_space}")
