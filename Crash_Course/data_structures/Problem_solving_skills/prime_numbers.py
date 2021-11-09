class PrimeNumber():
    """ Test if a given number is a prime number."""

    def __init__(self, number):
        self.number = number

    def prime_number(self):
        """ returns if a number is prime or not. """
        for i in range(2, self.number):
            if self.number % i == 0:
                return "It is not a prime number."
        return "It is a PRIME number."