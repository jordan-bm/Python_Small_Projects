# Jordan Burmylo-Magrann
# File: factorial.py
# Program: Finds n

def main():
        n = int(input('Enter a number: '))

        print(f'Loop-function return: {factorialLoop(n)}')

        print(f'Recursion-function return: {factorialRecursion(n)}')

def factorialLoop(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
        #print(f'{i=}, {factorial=}')
    return factorial

def factorialRecursion(n):
    if n == 0:
        return 1
    return n * factorialRecursion(n-1)

main()
