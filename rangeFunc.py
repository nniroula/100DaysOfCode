#!/Users/nabinniroula/anaconda3/bin/python

""" This work deals with the range() fucntion in Python. It is mostly used to generate list of numbers ."""

# range function works as an arguement for list() function  --- list( range() ).
x = list(range(10)) 
#print(x)

def rangeOfThousand():
    """ This generates the list of 1000 numbers. """
    numbs = list(range(1000))
    # print(numbs)
    # get the largest and smallest number from that list
    largestNum = max(numbs)
    print(f"The largest number in that range is ", largestNum)

    smallestNum = min(numbs)
    print(f"The smallest number in that range is ", smallestNum)

    return numbs
#print(rangeOfThousand())

# Create a list based on user input
def userList():
    """This function generates the list based on the user input. """
    # Get user input for the start, stop, and step values
    startVal = input("Please enter the starting number: ")
    # NOTE: input() function returns string, convert it to an integer using int() function.
    startVal = int(startVal)
    endVal = int(input("Please enter the ending number: "))
    stepVal = int(input("Please enter the stepping value: "))
    evenList = list(range(startVal, endVal, stepVal))
    return evenList
#print(userList())

# Create an even list and an odd list
def evenOrOddList():
    """ This function generates even or odd list based on the user stop value and interest. """
    stopVal = int(input("Enter your stop value: "))
    # input("Do you want even or odd list?\n")
    interest = input("Do you want even or odd list? (y/n):")
    evenlist = []
    oddlist = []
    if interest == 'y':
        for i in range(stopVal):
            if i%2 == 0:
                evenlist.append(i)
        return evenlist
    elif interest == 'n':
        for i in range(stopVal):
            if i % 2 == 1:
                oddlist.append(i)
        return oddlist
    else: # make user give input again.
        while(interest != 'y' or interest != 'n'):
            print("It is invalid input, please try y for even or n for odd again.")
            interest = input("Do you want even or odd list? (y/n):")
            if interest == 'y':
                for i in range(stopVal):
                    if i%2 == 0:
                        evenlist.append(i)
                return evenlist
            elif interest == 'n':
                for i in range(stopVal):
                    if i % 2 == 1:
                        oddlist.append(i)
                return oddlist

print(evenOrOddList()) 






