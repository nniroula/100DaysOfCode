#!/Users/nabinniroula/anaconda3/bin/python

""" Here, we will talk about __name__ == __main__. This means when running this file or module, only run and give output
for what is called underneath it. 
The advantage is when we have to import the file onto another file. """

def square(n):
    return n*n

# for i in range(10):
#     print(square(i))

# put for loop code inside main() so that when this file is run, it only executes the code inside for loop. 
def main():
    for i in range(10):
        print(square(i))
    
# now call only main function so that it executes only the code inside the main function
if __name__ == "__main__":
    main()


