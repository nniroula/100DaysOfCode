#!/Users/nabinniroula/anaconda3/bin/python

""" whatever is here deals with reading and writing to a file. """
# Create a file in the same directory and read it.

# readlines() method reads a file line by line and stores into a list. This displays newline \n characters
fileInput = open("myFile.txt")
readFile = fileInput.readlines()

#print(readFile)

# use read() method to read a blokc of content in a file. This does not produce new line character, \n.
fileToBeRead = open("myFile.txt")
readingFile = fileToBeRead.read()
fileToBeRead.close()

#print(readingFile)

# what happens if a file does not exist, gives an error message.
""" 
fileIn = open("good.txt")  # this file does not exist
# readThisFile = fileIn.readlines()
readThisFile = fileIn.read()
fileIn.close()
#print(readThisFile)
"""

""" Writing to a file in python """
# openFile = open("fileName", "w")
# openFile = open("fileName", "a")
# openFile = open("fileName", "r")

# write() function to write to a file

# steps - open a file, write to that file, and close that file
openFile = open("outputFile.txt", "w")
openFile.write('PROGRAMMING IS CHALLENGING. HOWEVER, IT IS FUN TOO. ')
openFile.close() 

# append text to the end of the file
openFileToAppend = open("outputFile.txt", "a")
openFileToAppend.write("\nCoding is going as a cr cr cr crazy work.")
openFileToAppend.close()





