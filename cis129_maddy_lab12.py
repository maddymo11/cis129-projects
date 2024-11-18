#Maddy Simonds
#11-18-24
#CIS 129 Lab 12 OOP
#This program will get info about a users pet
def main():
    animal = Pet() #create animal object

    #get values for pet
    inputName = input('Please enter a pet name:\n')
    animal.setName(inputName)

    inputType = input('Please enter pet type:\n')
    animal.setType(inputType)

    inputAge = input('Please enter pet age:\n')
    animal.setAge(inputAge)
    #show values for pet
    print('The pet name is',animal.getName())
    print('The pet type is',animal.getType())
    print('The pet age is',animal.getAge())

class Pet:
    #fields
    name = str
    type = str
    age = 0
    #constructor
    def __init__(self, n='', t='', a=0):
        self.name = n
        self.type = t
        self.age = a
#mutators (setters)
    def setName(self, n):
        self.name = n
    def setType(self, t):
        self.type = t
    def setAge(self, a):
        self.age = a
#accessors (getters)
    def getName(self):
        return self.name
    def getType(self):
        return self.type
    def getAge(self):
        return self.age

main()