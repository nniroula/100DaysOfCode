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

print(f"\tAfter Plus operation: {plus_ans}\n\tAfter minus operation is {minus_ans}\n\tAfter One Slash operation is \
{divide_ans_one_slash}\n\tAfter Two Slash operation is {divide_ans_two_slash}")




