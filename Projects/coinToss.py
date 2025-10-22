# Jordan Burmylo-Magrann
# File: coinToss.py
# Program: Tests fairness of randint function by simulating a coin toss

# Sample run:
# Tosses    Heads   Tails   Pr[Heads]   Pr[Tails]
# -----------------------------------------------
# 10        3       7       0.30        0.70
# 100       49      51      0.49        0.51
# 1000      506     494     0.51        0.49
# 10000     4979    5021    0.50        0.50
# 100000    50022   59978   0.50        0.50
# 1000000   499523  500477  0.50        0.50

from random import randint

# function : coinTosses
# Returns number of heads generated from a series of coinTosses
def coinTosses(limit):
    headCount = 0
    i = 1

    while i <= limit: # i = 1, 2, 3, 4, ...., limit = 10, 100, 1000, ....,
        if randint(0,1) == 0:
            headCount = headCount + 1
        #print(f'{i=}, {limit=}, {headCount=}') # Debugger
        i += 1

    return headCount

# MAIN

# Create a header of items to be listed
# print('--------------------------')

print(f'{'Tosses':<10}{'Heads':<10}{'Tails':<10}{'Pr[Heads]':<13}{'Pr[Tails]':<13}')
print('-'*53)

# Print number of heads, tails, and pr of each based on coin tosses in
# Multiples of 10

tosses = 10
maxTosses = 1000000
heads = 0 # holds number of heads
tails = 0 # holds number of tails

# While loop for toss change
while tosses <= maxTosses:
    heads = coinTosses(tosses)
    tails = tosses - heads
    print(f'{tosses:<10}{heads:<10}{tails:<10}{(heads/tosses):<13.2f}{(tails/tosses):<13.2f}')
    tosses *= 10
