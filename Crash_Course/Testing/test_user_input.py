import unittest
from user_input import UserInput

class TestUserInput(unittest.TestCase):
    """ This class tests the UserInput class."""

    def test_first_and_last_name(self):
        """ This fucntion tests the get_user_fname() """
        # Instantiate the class
        obj1 = UserInput()
        # call a method for first name
            # create a variable for the user name
        f_name = "Nabin"
        first_name = obj1.get_user_fname()
        self.assertEqual("Nabin", first_name.title())

unittest.main()
