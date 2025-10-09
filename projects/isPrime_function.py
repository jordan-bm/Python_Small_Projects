# Jordan Burmylo-Magrann
# File : function_isPrime.py
# Program: Given a positive integer greater than 1, determine whether prime or not prime

# Function : isPrime_function(num)
# Returns true if number is prime
# Returns false otherwise
from math import sqrt

def isPrime_function(num):
    if (num != 2) and (num % 2) == 0:
        return False
    else:
        factor = 3
        factorUpperBound = sqrt(num)

        while (factor <= factorUpperBound):
            if (num % factor == 0):
                return False
            factor = factor + 2

    return True


# Main
# Receive int to be tested
n = int(input('Enter positive integer greater than 1: '))

# Check if int is prime or composite
result = isPrime_function(n)

# Output result
if result == True:
    print(f'{n} is a prime integer')
else:
    print(f'{n} is a composite integer')
    
