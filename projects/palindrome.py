# Jordan Burmylo-Magrann
# File : palindrome.py
# Program: Checks whether the given alphanumeric string is a palindrome

def main():
    inp = input('Enter a string: ')

    print(isPalindrome(inp))

def isPalindrome(string):
    string = string.lower() # Remove case-sensitivity
    if len(string) == 1 or len(string) == 0:
        return True
    elif string[0] != string[-1]:
        return False
    else:
        return isPalindrome(string[1:-1])
        

main()
