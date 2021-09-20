#!/Users/nabinniroula/anaconda3/bin/python

# chekc if a number is odd or an even number

""" 
usser_input = int(input("Please enter your number: "))  # int() means for number

if usser_input % 2 == 0:
    print("It is an even number.")
elif usser_input % 2 == 1:
    print("It is an odd number.")
# else:
#     print("Invalid input, please try next time.")


# While loop

DONE = True
even_list = []
while DONE:
    user_input = input("Please Enter a number: ")
    if user_input.isdigit():   # isdigit() considers negative numbers as False value, it is a string function.
        user_input = int(user_input)
        if user_input > 0 and user_input < 100:
            # even_list = [i for i in range(user_input) if i%2 == 0]
            for i in range(user_input + 1):
                if i % 2 == 0:
                    even_list.append(i)
                else:
                    DONE = False
            break # break breaks out off the loop and stops execution
        else:
            print("invalid input, please try again below...")
            continue  # continue takes back to the top of the loop
    else:
        print("Not a valid input, try again ...")
        continue
print(even_list)
     

unconfirmed_user = ["John", "Jackie", "katie"]
confirmed_user = []
for user in unconfirmed_user:
    if user not in confirmed_user and len(user) > 0:
        confirmed_user.append(user)
        print(f"Confirming  a user {user.title()}")
print("The following users are confirmed:")
for name in confirmed_user:
    print(f"\t{name.title()}")

"""

# Dictionaries
# get user input and use to test the poll result
cric_poll = {}
# name = input("Enter your name please: ")
# team = input("What is favorite IPL cricket team? ")

DONE = True
while DONE:
    name = input("Enter your name please: ")
    team = input("What is favorite IPL cricket team? ")
    cric_poll[name] = team
    repeat = input("Would you like to continue the poll? (yes/no) ")
    if repeat.lower() == "yes":
        continue
    elif repeat.lower() == "no":
        DONE = False
    else:
        break
print(cric_poll)




