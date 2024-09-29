# Maddy Simonds
# CIS 129 Lab 5
# 9-29-24
# This program will keep track of the number of water bottles a grocery store collected for 7 days
keepGoing = 'y'
# ^ this variable will be used to run the program again
NBR_OF_DAYS = 7
repeat = True
#this will repeat the program if the user wants to input another week's data
while repeat:
    counter = 1
    totalBottles = 0
    todayBottles = 0
    totalPayout = 0
    # ^ initializing variables
#this code will prompt the user to enter the number of bottles for each day in the week
    while counter <= NBR_OF_DAYS:
        dayPrompt = f'Enter number of bottles for day #{counter}: '
        todayBottles = int(input(dayPrompt))
        counter += 1    
        totalBottles += todayBottles
#this calculates the payout and prints the payout and total info
    totalPayout = float(f'{totalBottles * .10:.1f}')
    print('\nThe total number of bottles collected is', totalBottles)
    print('The total paid out is $', totalPayout)
#this determines if the program will be repeated
    keepGoing = input('\nDo you want to enter another week\'s worth of data?\n(Enter y or n): ')
    if keepGoing == 'y':
        repeat = True
    else:
        repeat = False
    print('')