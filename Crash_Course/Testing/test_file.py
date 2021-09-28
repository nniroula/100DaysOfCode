
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

# test the class AnnoymousSurvey
import unittest
from file_to_test import AnnonymousSurvey # this is a class in that file

# test that resonse is in list of responses after it is appended, use assetIn()

class TestAnnonymousSurvey(unittest.TestCase):
    # Test AnnonymousSurvey class.  # this must be a docstring
    # define a function to test it
    def test_single_response_is_in_list(self):
        #test if the list responses holds a given response. # this must be a docstring
        # To test it we need a question and an instance of that class
        question = "What language you feel comfortable with: "
        annoymous_survey = AnnonymousSurvey(question)
        # take a response and store it in a list by calling a function to store it
        annoymous_survey.store_response('Python')  # our response is Python
        # now check if store_response() function has put Python in a list
        self.assertIn("Python", annoymous_survey.responses)

    #Now test if three responses are stored in a list
    def test_store_three_responses(self):
        qustion2 = "Give 3 programming languages: "
        # isntantiate a class
        obj = AnnonymousSurvey(qustion2)
        # now use a function to store multiple responses
        res = ["Python", "JS", "C++"]
        # store the responses in a list
        for item in res:
            obj.store_response(item) 
        # test that these reponses are stored properly
        for respond in obj.responses:
            self.assertIn(respond, obj.responses)

unittest.main()  # without this statement the test runs, but you may not be able to see the output in terminal.

# Different and much efficient approach is use setUp() method to instantiate a class, and create responses


import unittest
from file_to_test import AnnonymousSurvey # this is a class in that file

class TestAnnonymousSurvey(unittest.TestCase):
    """ Test AnnonymousSurvey class. """
    # define  a setUP() method
    def setUp(self):
        # instanatiate a class
        question = "What is your best programming language? "
        self.instance_of_class = AnnonymousSurvey(question) # self means available for all methods in a class
        # create a list of responses so that you can use them in different test methods
        self.res = ["JS", "Python", "C++"] # becasue it has self prefix, we can use it in all methods within a class
    # define a function to test it
    def test_single_response_is_in_list(self):
        """ test if the list responses holds a given response. """
        # To test it we need a question and an instance of that class
       
        # take a response and store it in a list by calling a function to store it
        self.instance_of_class.store_response(self.res[0])  # our response is Python
        # now check if store_response() function has put Python in a list
        self.assertIn(self.res[0], self.instance_of_class.responses)

    #Now test if three responses are stored in a list
    def test_store_three_responses(self):
        for respond in self.res:
            # append to the given list by calling an assigned function
            self.instance_of_class.store_response(respond)
        # now test that all the responses are in the list
        for item in self.instance_of_class.responses:
            self.assertIn(item, self.instance_of_class.responses)

unittest.main()
