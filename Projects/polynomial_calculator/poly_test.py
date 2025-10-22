# Jordan Burmylo-Magrann
# File: poly_test.py
# Program: Polynomial listing

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

def read_poly(filename):
    openFile = open(filename, 'r')
    fileStr = openFile.read() # creates string of all info in file
    fileList = fileStr.split() # splits string by spaces into seperate list items
    #print(fileList) # debug
    
    for i in range(len(fileList)): # accessing all index positions
        fileList[i] = fileList[i].strip('\n') # stripping white space characters
        fileList[i] = int(fileList[i]) # integerizing each item
    #print(fileList) # debug
    
    p = [0] * (fileList[0] + 1) # creates list length of highest degree in poly + 1 (for 0 exponent)
    #print(p) # debug
    #print(len(p)) # debug
    
    for index in range(len(fileList)): # exponents in list are starting at 0 every other (0, 2, 4, ...)
        # exponents of poly (any positive index) will be used to index coeffecient positions in list 'p'
        # coeffecients for each exponent (index) are index + 1
        #print(index) # debug
        if (index % 2 == 0) or index == 0: # only accessing exponent positions
            p[fileList[index]] = fileList[index + 1]
    #print(p) # debug
    return p


def print_poly(p): # polynomial p
    #print(p) # debug
    nonZeroList = []
    for num in range(len(p)):
        #print(num, end = ' ') # debug
        if p[num] != 0:
            nonZeroList.insert(0, num) # creating list of all indexes that have coeffecients 
            # indexes are exponents, coeffecients are p[index]
    #print(nonZeroList) # debug
    
    polynomial = ''
    if nonZeroList[0] != 0 and nonZeroList[0] != 1:
        polynomial = str(p[nonZeroList[0]]) + 'x^' + str(nonZeroList[0])
    elif nonZeroList[0] != 0 and nonZeroList[0] != 1 and (p[0] == 1 or p[0] == -1):
        polynomial = 'x^' + str(nonZeroList[0])
    #print(polynomial) # debug
    
    for i in nonZeroList[1:]: # accessing everything but index 0 (already in string if exponent isn't 0 or 1)
        #print(i) # debug
        
        if i != 0 and i != 1:
            if p[i] < 0: # negative coeffecients
                if p[i] == -1:
                    polynomial += ' - ' + 'x^' + str(i)
                else:
                    polynomial += ' - ' + str(abs(p[i])) + 'x^' + str(i)
            else: # positive coeffecients
                if p[i] == 1:
                    polynomial += ' + ' + 'x^' + str(i)
                else:
                    polynomial += ' + ' + str(abs(p[i])) + 'x^' + str(i)
        elif i == 1: # x attached to coeffecient, no exponent necessary
            if p[i] < 0:
                if p[i] == -1:
                    polynomial += ' - ' + 'x'
                else:
                    polynomial += ' - ' + str(abs(p[i])) + 'x'
            else:
                if p[i] == 1:
                    polynomial += ' + ' + 'x'
                else:
                    polynomial += ' + ' + str(abs(p[i])) + 'x'
        else: # (i == 0), just coeffecient, no x or exponent necessary
            if p[i] < 0:
                polynomial += ' - ' + str(abs(p[i]))
            else:
                polynomial += ' + ' + str(abs(p[i]))
    print(polynomial) 
    
    
    
def eval_poly(p, r): # polynomial p, real num r
    # redoing nonZeroList code 
    nonZeroList = []
    for num in range(len(p)):
        #print(num, end = ' ') # debug
        if p[num] != 0:
            nonZeroList.insert(0, num) # creating list of all indexes that have coeffecients 
            # indexes are exponents, coeffecients are p[index]
    #print(nonZeroList) # debug
    
    sum = 0
    for index in nonZeroList:
        if index != 1 and index != 0:
            sum += p[index] * (r ** index)
        elif index == 1:
            sum += p[index] * r
        else:
            sum += p[index]
    #print(sum) # debug
    return sum

def scale_poly(p, s): # polynomial p, real num s
    #print(p) # debug
    sp = p[:] # copying polynomial list for editing
    for num in range(len(p)):
        if p[num] != 0:
            sp[num] *= s # scaling itself by s
    #print(sp) # debug
    #print(p) # debug
    return sp 

def sum_poly(p1, p2): # polynomial p1 & p2
    sum_ = []
    #print(p1, p2) # debug
    #print(len(p1), len(p2)) # debug
    if len(p1) > len(p2): # p1 is larger
        new_p2 = p2 + ([0] * (len(p1) - len(p2)))
        #print(new_p2) # debug
        for i in range(len(p1)):
            sum_.append(p1[i] + new_p2[i])      
    elif len(p1) < len(p2): # p2 is larger
        new_p1 = p1 + ([0] * (len(p2) - len(p1)))
        #print(new_p1) # debug
        for i in range(len(p2)):
            sum_.append(new_p1[i] + p2[i])
    else: # they're equal
        for i in range(len(p1)):
            sum_.append(p1[i] + p2[i])
    #print(sum_) # debug
    return sum_
            

def diff_poly(p1, p2): # polynomial p1 & p2
    diff = []
    #print(p1, p2) # debug
    #print(len(p1), len(p2)) # debug
    if len(p1) > len(p2): # p1 is larger
        new_p2 = p2 + ([0] * (len(p1) - len(p2))) 
        #print(new_p2) # debug
        for i in range(len(p1)):
            diff.append(p1[i] - new_p2[i])
            
    elif len(p1) < len(p2): # p2 is larger
        new_p1 = p1 + ([0] * (len(p2) - len(p1))) 
        #print(new_p1) # debug
        for i in range(len(p2)):
            diff.append(new_p1[i] - p2[i])
    else: # they're equal
        for i in range(len(p1)):
            diff.append(p1[i] - p2[i])
    #print(diff) # debug
    return diff


def test_polys():
    answer = "y"
    while (answer[0].lower() == "y"):
        print("                  ------------------------------")
        print("                   Testing Polynomial Functions ")
        print("                  ------------------------------")
        print(" ")
        print("I will first create two polynomials. You will")
        print("be asked to provide the names of the files   ")
        print("containing the polynomial data.")
        print(" ")
        filename = input("Enter the name of the first file: ")
        p1 = read_poly(filename)
        print("The first polynomial has been read, printed below: ")
        print_poly(p1)
        print(" ")
        filename = input("Enter the name of the second file: ")
        p2 = read_poly(filename)
        print("The second polynomial has been read, printed below: ")
        print_poly(p2)
        print(" ")
        print("Each of the remaining function implementations will")
        print("now be tested. Check the output to make sure that ")
        print("your function is producing the correct answer.")

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("               -----------------------")
        print("                  Testing eval_poly")
        print("               -----------------------")
        print("The first polynomial evaluated at x = 0 gives ", eval_poly(p1, 0))
        print("The first polynomial evaluated at x = 2 gives ", eval_poly(p1, 2))
        print("The first polynomial evaluated at x = -1 gives ", eval_poly(p1, -1))

        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  ------------------------")
        print("                     Testing scale_poly   ")
        print("                  ------------------------")    
        sp = scale_poly(p1, 2)
        print("The first polynomial scaled by 2 is as follows:")
        print_poly(sp)

        print(" ")
        dummy = input("Hit the enter key to continue.")
        print(" ")
        print("                  ----------------------")
        print("                     Testing sum_poly   ")
        print("                  ----------------------")
        sum = sum_poly(p1, p2)
        print("(Sum) first polynomial + second polynomial equals: ")
        print_poly(sum)
        
        print(" ")
        dummy = input("Hit enter key to continue.")
        print(" ")
        print("                  -----------------------")
        print("                     Testing diff_poly   ")
        print("                  -----------------------")
        diff = diff_poly(p1, p2)
        print("(Difference) first polynomial - second polynomial equals: ")
        print_poly(diff)
        
        print(" ")
        answer = input("Run the tests again? [y/n] ")
    
    print("Goodbye!")
    

# main
test_polys() # main call

#Debugs
#read_poly(input()) # read_poly debug
#print_poly(read_poly(input())) # print_poly debug
#eval_poly(read_poly(input()), 2) # eval_poly debug
#scale_poly(read_poly(input()), 2) # scale_poly debug
#sum_poly(read_poly(input()), read_poly(input())) # sum_poly debug
#diff_poly(read_poly(input()), read_poly(input())) # diff_poly debug