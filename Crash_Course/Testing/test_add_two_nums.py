import unittest
from add_two_nums import AddTwoNumbers

class TestAddTwoNumbers(unittest.TestCase):
    def test_get_sum(self):
        # instantiate the class
        inst = AddTwoNumbers()
        # call method on that class
        sum1 = inst.get_sum()
        self.assertTrue(sum1)  
    
    def test_two_values(self):
        obj = AddTwoNumbers()
        sum2 = obj.get_sum()
        self.assertTrue(sum2)
        
unittest.main()
