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

obj1 = PrimeNumber(10)
result1 = obj1.prime_number()
print(result1)

obj2 = PrimeNumber(13)
result2 = obj2.prime_number()
print(result2)