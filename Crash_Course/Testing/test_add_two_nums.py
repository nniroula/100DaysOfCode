import unittest
from add_two_nums import AddTwoNumbers

class TestAddTwoNumbers(unittest.TestCase):
    def test_get_sum(self):
        # instantiate the class
        inst = AddTwoNumbers()
        # call method on that class
        sum1 = inst.get_sum()
        self.assertTrue(sum1)  

unittest.main()
