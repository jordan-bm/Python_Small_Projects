# Jordan Burmylo-Magrann
# File: netId.py
# Program: Generates user netID, email address and temporary password

# netID: generated using first letter of the first name followed by the last name
# email: netID@camden.rutgers.edu
# password : last 4 digits of ssn followed by first 3 letters of first name

# Sample Run:
# Enter your name: Jane Doe
# Enter social security number: 019-23-4567

# Your netID, email and temporary password are the following
# netID: JDoe
# email: JDoe@camden.rutgers.edu
# password: 4567Jan


# get user name and ssn
name = input('Enter First and Last Name: ').strip().title()
ssn = input('Enter ssn (xxx-xx-xxxx): ')
#print(name, ssn) # debug

# Create list of tokens

nameTokens = name.split() # splitting string into list with first/last name seperate
ssnTokens = ssn.split('-')
#print(nameTokens, ssnTokens) # debug

# generate user netID, email address and contemporary password
netID = ''.join([nameTokens[0][0], nameTokens[1]])
email = '@'.join([netID, 'camden.rutgers.edu'])
password = ''.join([ssnTokens[-1], nameTokens[0][0:3]])
print(f'Temporary netID: {netID}')
print(f'Temporary email: {email}')
print(f'Temporary password: {password}')
