#Maddy Simonds
#CIS129 Mod 11 Lab
#11-27-24

#Exercise 9.3
#write code that enables an instructor to enter each student’s first name and last name as strings
#and the student’s three exam grades as integers.


import csv
#open in append mode to add data to file
with open ('grades.csv', 'w', newline = '') as grades:
    
    #create writer object
    writer = csv.writer(grades)

    #get student info, loop until all data is entered
    while True: 
        firstName = input("Please enter student's first name:\n")
        lastName = input("Please enter student's last name:\n")
        studentName = [firstName, lastName]

        #nested while loop for exam scores
        examScores = [] #create empty list to store exam scores
        while len(examScores) < 3:
            try:
                getScores = (input(f"Please enter exam {len(examScores)+1} score:\n"))
                examScores.append(getScores)
            except ValueError:
                print('Invalid input, please enter an integer.')

        exam1, exam2, exam3 = examScores #label exam scores within list

        rowData = [firstName, lastName, exam1, exam2, exam3] #concatenate for student data

        #write student data to file
        writer.writerow(rowData)

        #loop if user has more students to record
        break_flag = bool
        while True:
            moreStudents = input('Would you like to record another student? Enter (y/n)\n')
            if moreStudents == 'n':
                break_flag = True
                break
            elif moreStudents =='y':
                break_flag = False
                break
            else:
                print('Please enter y or n.')
        #if user chooses n break outer loop
        if break_flag == True:
            break

with open('grades.csv', 'r') as grades:
    reader = csv.reader(grades)
    #loop through each record
    for row in reader:
        #display
        print(row)