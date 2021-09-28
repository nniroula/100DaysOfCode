# try-except is used to handle an unexptected error so that program cointinues executing.

# print(5/0)  # this statement gives error, but the try-except handles this.

"""
try:
    print(5/0)
except:
    print("You cannot divide by zero.")



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


# put this in a function
def count_file_words(filename):
    #Count the number of words in a file.
    # open the file, read it and return the word count
    try:
        with open(filename) as file_object:
            words_list = file_object.read()
            words_list = words_list.split()
            # print(len(words_list))
    except FileNotFoundError:
        return f"The file {filename} does not exist."
    else:
         return f"The total words count in the file {filename} is {len(words_list)}."

# call a function
word_count = count_file_words("names.txt")
# print(f"The words count in the file {} is {word_count}")

# run this function to count words in different files
files = ["names.txt", "ok.txt", "programming.txt"]
for file in files:
    func_apply = count_file_words(file)
    print(func_apply)

"""

