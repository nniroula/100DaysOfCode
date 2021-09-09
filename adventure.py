#!/Users/nabinniroula/anaconda3/bin/python

""" The game of take your own adventures. """

user_name = input("Please enter your name: ")
print(f"Hello, {user_name} welcome to the game of fun :) ")

user_input = input("You are in the tech fun ocean, type Y to dive in and N to opt out to do something else: ")

if user_input.lower() == 'y':
    print("Let's play it. ")
    question_ans = input(" What is '1' + '1' equals to? ")
    if question_ans == '11':
        print("Your in CS TRAP, try to escape it. ")
        question_ans = input(" Is Polimorphism part of OOP? [yes/no] ")
        if question_ans.lower() == "yes":
            print("You seem to be a true developer.")
            question_ans = input("Then what is an instance of a class called? ")
            if question_ans == object or question_ans == obj:
                print("Start coding your own adventure, what are you waiting for.")
            else:
                print("RELAX and find something else to do in your life. ")
        else:
            print("I believe you have to improve on your CS concpets. ")
            print("No questions for you. GOODBYE!!!!")  
    else:
        print("Oh, boring start. Not a problem. Catch up next time. ")
        ans_question = input("Give a commonly used one letter word? ")
        if ans_question.lower() == "i":
            print("Hillarous, continue ahead. ")
            ans_question = input("What is 'i' in CS world? ")
            if ans_question.lower() == 'string' or ans_question.lower() == 'str':
                print("Learning CS and programming is a fun thing. Code choose your own adventure game. ")
            else:
                print("It is not late to learn CS. Goodby!!!")

        else:
            print("Dummy Dum, can you think of a first person singular> ")

else:
    print("Good for you, we have a fun tour here. Just explore it and enjoy as much as you can.")
    ans_question = input("Enter a place: ")
    if len(ans_question) <= 3:
        print("You are a lazy fool. We cannot move ahead with such a lazy person. Sorry!")
    else:
        print("Good job, stay enthusiastic and move ahead. ")
        ans_question = input("Enter a name of a river: ")
        if len(ans_question) >= 0:
            print("You are now on the other side of the river, think carefully.")
            ans_question = input("How do you get back to the place that you chose earlier? ")
            if ans_question.lower() == "plane" or ans_question.lower() == "flight" or ans_question == "fly":
                print("Good job, but in your second step you missed a chance for making a excited CS journey. Thanks")
            else:
                print("Could even think of a plane in this modern world. Use your mind.")
        else:
            print("Sorry, you cannot play this game. ")

