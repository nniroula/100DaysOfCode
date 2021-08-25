#!/Users/nabinniroula/anaconda3/bin/python

class QuizGame:
    """ It will ask user the questions, and at the end provides the score based on the correct answers."""

    score = 0
    choice = input("Do you want to play a game [yes/no]: ").lower()
    if choice == "no":
        quit()
    else:
        print("It is a quiz, answer the following questions.")
        
        print("Question 1: ")
        ans = input("What is a VS Code? ")
        # ans = ans.lower()
        if ans.lower() == "Text editor".lower():
            print("Correct")
            score += 1
        else:
            print("Wrong answer")
        
        print("Question 2: ")
        ans = input("What is an instance of a class called? ")  
        if ans.lower() == 'Object'.lower():
            print("Correct")
            score += 1
        else:
            print("Wrong answer")

        print("Question 3: ")
        ans = input("What is the blue print of an object called in OOP? ")
        if ans.lower() == "Class".lower():
            print("Correct")
            score += 1
        else:
            print("Wrong answer")
        
        print("Question 4: ")
        ans = input("Is python an OOP language? ").lower()
        if ans.lower() == "yes":
            print("Correct")
            score += 1
        else:
            print("Wrong answer")

        print("Question 5: ")
        ans = input("Is Python Front end or Back end language? ")
        if ans.lower() == "Back end".lower():
            print("Correct")
            score += 1
        else:
            print("Wrong answer")

    print(f"Score = {score}/5.")
        

