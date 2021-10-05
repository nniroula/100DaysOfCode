from fabonacci import FabonacciNumber
import unittest

class TestFabonacci(unittest.TestCase):
    """This class will test the Fibonnaci class defined in fabonacci.py file."""
    def setUP(self):
        # instantiate a class
        self.obj = FabonacciNumber(3)

    def test_fabinacci_pattern(self):
        """ It tests fabinacci_pattern function."""
        obj = FabonacciNumber(3)
        result = obj.fabonacci_pattern()
        self.assertEqual([0, 1, 1], result)
    
    def test_display_fabonacci_numbers(self):
        """ It tests display_fabinnaci_numbers function."""
        obj2 = FabonacciNumber(1)
        result2 = obj2.display_fabonacci_numbers()
        self.assertTrue(result2)

unittest.main()


