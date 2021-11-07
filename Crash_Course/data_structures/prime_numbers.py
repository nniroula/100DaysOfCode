def prime_numbers(self, num):
    factors = []
    for i in range(2, num + 1):
        if num % i == 1:
            factors.append(i)

