import unittest
# from try_except_for_testing import TryExcept
from try_except_for_testing import TryExcept

class TestTryExceptForTesting(unittest.TestCase):
    def test_return_quotient(self):
        obj1 = TryExcept(2, 3)
        result = obj1.return_quotient()
        self.assertEqual(1.5, result)

unittest.main()
