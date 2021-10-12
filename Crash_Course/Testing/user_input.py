class UserInput():
    """ This class takes user input. """

    def __init__(self):
        self.fname = " "
        self.lname = " "

    def get_user_fname(self):
        self.fname = input("Please enter your first name: ")
        return self.fname

    def get_user_lname(self):
        self.lname = input("Please enter your last name: ")
        return self.lname

    def full_name(self):
        full_name = self.get_user_fname().title() + " " + self.get_user_lname().title()
        return full_name

# object
# name1 = UserInput()
# first_name = name1.get_user_fname()
# print(first_name)
# full_name = name1.full_name()
# print(full_name)