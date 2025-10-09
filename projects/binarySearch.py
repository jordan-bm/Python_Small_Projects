# Jordan Burmylo-Magrann 
# File: binarySearch.py
# Program: Finds an element z in a sorted list L

def main():

    sortedList = [1, 3, 5, 6, 7, 9, 11, 14, 15, 18, 20, 23, 25, 29, 30]

    num = int(input('number: '))

    print(binarySearch(sortedList, num))


def binarySearch(l, n):
    mid = len(l) // 2
    #print(mid) # debug
    if len(l) == 0: # base case
        return False
    elif l[mid] == n:
        return True
    elif n < l[mid]:
        return binarySearch(l[:mid], n)
    elif n > l[mid]:
        return binarySearch(l[mid+1:], n)

main()
