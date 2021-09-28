"""
import unittest
# import file_to_test # OR
from file_to_test import full_name
# fullname = full_name("Nabin", "Niroula")
# create a class to test the full_name function
class TestFullName(unittest.TestCase):
    # Test a file file_to_test.py  # this should be a docstring
    # define a function to test a function given in file_to_test.py
    def test_full_name(self):
        # test the full_name function # this must be a docstring
        fullname = full_name("Nabin", "niroula")
        self.assertEqual(fullname, "Nabin Niroula")

    # add a test to test a name with a middle name included
    def test_first_middle_last(self):
        first_middle_last = full_name("Charles", "John", "Smith")
        self.assertEqual(first_middle_last, "Charles Smith John")

unittest.main()

"""
# test the class AnnoymousSurvey
import unittest
from file_to_test import AnnonymousSurvey # this is a class in that file

# test that resonse is in list of responses after it is appended, use assetIn()

class TestAnnonymousSurvey(unittest.TestCase):
    """ Test AnnonymousSurvey class. """
    # define a function to test it
    def test_single_response_is_in_list(self):
        """ test if the list responses holds a given response. """
        # To test it we need a question and an instance of that class
        question = "What language you feel comfortable with: "
        annoymous_survey = AnnonymousSurvey(question)
        # take a response and store it in a list by calling a function to store it
        annoymous_survey.store_response('Python')  # our response is Python
        # now check if store_response() function has put Python in a list
        self.assertIn("Python", annoymous_survey.responses)
unittest.main()
