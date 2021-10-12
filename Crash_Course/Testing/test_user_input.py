import unittest
from user_input import UserInput

class TestUserInput(unittest.TestCase):
    """ This class tests the UserInput class."""

    def test_first_and_last_name(self):
        """ This fucntion tests the get_user_fname() """
        # Instantiate the class
        obj1 = UserInput()
        # call a method for first name
        first_name = obj1.get_user_fname()
        self.assertTrue(first_name.title())

    def test_last_name(self):
        """ This function tests the user's last name """
        obj2 = UserInput()

        last_name = obj2.get_user_lname()
        self.assertTrue(last_name)

unittest.main()
