"""
def full_name(first, last, middle=""):
    # return a full name of a person  # this should be a doctstring
    if middle:
        return first.title() + " " + middle.title() + " " + last.title()
    else:
        return first.title() + " " + last.title()
get_name = full_name("Nabisha", "Niroula")
# print(get_name)
# now test this function in a test file

"""

# next write a class and test it
class AnnonymousSurvey():
    """ Collects anonymous answers to a survey question."""
    
    def __init__(self, question):
        """ Stores a question and prepares to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """ show the question."""
        return self.question
    
    def store_response(self, new_response):
        """ Store a single response to a survey."""
        self.responses.append(new_response)

    def show_results(self):
        """ Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('-' + response)
        
# make an instance ot this class
# survey_question = "Are you happy coding? "
# # show the question
# annonymous_survey = AnnonymousSurvey(survey_question)
# show_q = annonymous_survey.show_question()
# print(show_q)

# Store responses to a question -use class.function_for_responses ()
# print("Type q to quit any time\n")
# while True:  # this means while response list is empty
#     response = input("Answer: ")
#     if response == 'q':
#         break
#     annonymous_survey.store_response(response)
# # check if responses holds enetered responses
# res = annonymous_survey.responses
# print(res)

# Now, write unit tests to see if any one aspect of this class behaves as expected.



    