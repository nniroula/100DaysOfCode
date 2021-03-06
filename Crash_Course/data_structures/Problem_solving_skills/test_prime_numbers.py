import unittest
from prime_numbers import PrimeNumber

class TestPrimeNumber(unittest.TestCase):
    """ tests if PrimeNumber class returns a prime number. """

    def test_prime_number(self):
        """ tests if a prime_number function gives a correct output. """
        # instantiate the class
        obj1 = PrimeNumber(7)
        # call a method on this object
        result1 = obj1.prime_number()
        self.assertTrue(result1)

    def test_not_prime(self):
        obj2 = PrimeNumber(10)
        result2 = obj2.prime_number()
        self.assertEqual('It is not a prime number.', result2)

unittest.main()
