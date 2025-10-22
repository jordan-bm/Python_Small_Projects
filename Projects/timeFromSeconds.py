# Jordan Burmylo-Magrann
# File: timeFromSeconds.py
''' Program: Takes an input of some number of seconds from the 
start of the day and returns the time in hours:minutes:seconds using
military time (1pm is 13:0:0, 1 am is 1:0:0) '''

# 0 seconds should output 0:0:0
# 60 seconds should out put 0:1:0
# 3600 seconds should output 1:0:0
# 75 seconds       0:1:15


# Get time in seconds
time_in_seconds = int(input('Please enter time in seconds:'))

# Calculate hours minutes and seconds
hours= time_in_seconds // 3600
minutes= (time_in_seconds // 60) % 60
seconds = time_in_seconds % 60

# Output time in military time format (hours:minutes:seconds)
military_time=str(hours) + ':' + str(minutes) + ':' + str(seconds)
print('The time is', military_time)

# or print(f'The time is {hours}:{minutes}:{seconds}')
