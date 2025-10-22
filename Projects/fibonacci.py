# Jordan Burmylo-Magrann
# File: fibonacci.py
# Program: Finds n'th Fibonacci number

# Fibonacci seq: 1, 1, 2, 3, 5, 8, 13, 21, 34, ....

def main():

    n = int(input('n: '))

    print(fibonacciRecursion(n))



def fibonacciRecursion(n):
    if n == 1 or n == 2:
        return 1
    return fibonacciRecursion(n-1) + fibonacciRecursion(n-2)





main()
