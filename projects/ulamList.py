# Jordan Burmylo-Magrann
# File: ulamList.py
# Program: receive input positive integers, return Ulam sequence of those integers (spaced correctly)

# if int is even then the next number in the sequence is int/2
# if int is odd then the next number in the sequence is 3int + 1
# right align each 10 columns by 7


def ulam(n): # main function, calls ulam_seq inside to generate seq, but takes that info and prints
    ulamList = ulam_seq(n)
    print(f"Ulam's sequence for {n}:")
    
    columns = 0
    for i in ulamList:
        #print(i) # debug
     
        print(f'{i:>7}', end = ' ')
        columns += 1
        
        if columns == 7:
            print()
            print()
            columns = 0
    print()
    
            

def ulam_seq(n): # generates list of full ulam sequence for num (to be used in ulam in a loop for printing)
    ulamList = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
            ulamList.append(n)
        else:
            n = int((3 * n) + 1)
            ulamList.append(n)
    #print(ulamList) # debug
    return ulamList
    
if __name__ == "__main__":
    print(f'Input positive integer (or 0 to end the program):', end = ' ')
    num = int(input())
    if num == 0:
        print(f'Thank you for using the program.')
    else:
        while num > 0: # receiving input integers in a loop, calling main function in loop 
            ulam(num) # calling main function - will call sequence function inside, use that list to print
            #ulam_seq(num) # test for correct lists
            #print(num) # debug
            print(f'Input positive integer (or 0 to end the program):', end = ' ')
            num = int(input())
        print(f'Thank you for using the program.')
        
