import unittest
from try_except_for_testing import TryExcept

class TestTryExceptForTesting(unittest.TestCase):
    def test_return_quotient(self):
        "Test return_quotient function. "
        obj1 = TryExcept(2, 3)
        result = obj1.return_quotient()
        self.assertEqual(1.5, result)
    
    def test_zero_division(self):
        """Test code in try-except block."""
        obj2 = TryExcept(0, 2)
        result2 = obj2.return_quotient()
        self.assertEqual("Zero Divison not allowed.", result2)

unittest.main()
