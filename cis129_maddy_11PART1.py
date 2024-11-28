#Maddy Simonds
#CIS129 Mod 11 Lab (9.1 and 9.2)
#11-27-24

#Exercise 9.1, write code that enables you to store any # of grades into a grades.txt plain text file

#create file
with open('grades.txt', 'w+') as grades:
    #retrieve any number of grades
    keepGoing = 'y'
    while True: 
        oneGrade = input("Please enter student grade, or type 'exit' to stop:\n")

        if oneGrade == 'exit':
            break

        grades.write(oneGrade + '\n') #write each new grade to file on new line


#Exercise 9.2
#write code that reads the grades from the text file, then display the individual grades and their total, count, and average

from collections import Counter #used to find frequency of each grade
#open file in reading mode
with open('grades.txt', 'r') as grades:
    total = 0 #used to find average
    counter = 0 #used to find average
    soloGrades = [] #list to store grades for freq count

    #iterate over each line 
    for grade in grades:
    #read all lines and strip \n characters
        grade = grade.strip()
        soloGrades.append(grade) #add each grade to list
        total += int(grade)
        counter +=1
        if counter > 0: #avoid zerodivisionerror if there are no grades
    #calculate average
            classAverage = (total / counter)
    #display average and total count
    print(' ')
    print('*' * 30)
    print(f'{'Class Average: '}{classAverage:.2f}')
    print('Total Grades: ',counter, '\n')


#use counter to find frequency
    gradeCounts = Counter(soloGrades)

#display individual grades and the number of occurences for each grade
    print(f'{'Grades':<10}{'Frequency':>10}')
    for grade, count in gradeCounts.items():
        print(f'{grade:>6}{count:>14}')
