# Jordan Burmylo-Magrann
# File: recursion_findnum.py
# Program: Finds if a number is in the given list (recursively)

def main():
    alist = [1, 4, 6, 23, 56, 45, 78, 99, 101, 0, 32, 21]
    #alist = []

    n = int(input('n: '))

    print(find(alist, n))


def find(alist, n):
    if len(alist) == 0:
        return False
    elif alist[0] == n:
        return True
    else:
        return find(alist[1:], n)

main()
