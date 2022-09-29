"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError(f"Number_of_primes:{number_of_primes} is less than or equal 0")
    list = []
    counter = 2
    while len(list) < number_of_primes:
        # check if a number is prime
        isPrime = True
        j = 0
        while isPrime and j < len(list):
            if counter % list[j] == 0:
                isPrime = False
            j += 1

        if isPrime:
            list.append(counter)
        counter += 1
    return list
