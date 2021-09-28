# try-except is used to handle an unexptected error so that program cointinues executing.

# print(5/0)  # this statement gives error, but the try-except handles this.

"""
try:
    print(5/0)
except:
    print("You cannot divide by zero.")

"""

# counting words in text file
try:
    file = "names.txt"
    with open(file) as read_file:
        file_content = read_file.read()
        # now split the string into a list
        get_words = file_content.split()
        get_length = len(get_words)     
except FileNotFoundError:
    print(f"the file {file} does not exist. ")
else:
    print(f"the length of a file is {get_length}")