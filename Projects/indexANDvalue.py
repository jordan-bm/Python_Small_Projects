# Jordan Burmylo-Magrann
# File: indexANDvalue.py
# Program: Retrieves both the index and value from a list

fruits = ['apples', 'oranges', 'kiwi', 'grape', 'bananas']
# index =   0           1         2      3           4
# value = apples      oranges    ....
print('for index in range(len(fruits))')

for i in range(len(fruits)): # i -> 0, 1, 2, ...
    name = fruits[i]
    print(f'{i}:{name}')
print()
               
# gets name of fruit
for name in fruits: # name -> apples,...
    i = fruits.index(name)
    print(f'{i}: {name}')
print()

# gets both index name
print('for (index, name) in enumerate(fruits)')
for (i, name) in enumerate(fruits):
    print(f'{i}: {name}')
print()
