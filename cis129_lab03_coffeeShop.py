#Author: Maddy Simonds
#Module 3 Lab in my CIS129 course
#this program is an interactive text-based coffee shop simulator
#x represents cost of coffees
#y represents cost of muffins
#s represents cost of scone
#z represents cost of tea
x = 5
y = 4
s = 4
z = 3
coffeeAmount = int(input('Number of coffees bought?'))
muffinAmount = int(input('Number of muffins bought?')) 
sconeAmount = int(input('Number of scones bought?'))
teaAmount = int(input('Number of teas bought?'))
subTotal = int((x * coffeeAmount) + (y * muffinAmount) + (s * sconeAmount) + (z * teaAmount))
#function adds the total cost of all variables
#subTotal represents total before tax
total = subTotal + (subTotal * .06) 
#function adds subTotal and tax to make the final total
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
print(coffeeAmount)
print('Number of muffins bought?')
print(muffinAmount)
print('Number of scones bought?')
print(sconeAmount)
print('Number of teas bought?')
print(teaAmount)
print('***************************************\n\n***************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffeeAmount, 'Coffee at $5.00 each: $',int(x * coffeeAmount),'.00')
print(muffinAmount, 'Muffin at $4.00 each: $',int(y * muffinAmount),'.00')
print(sconeAmount, 'Scone at $4.00 each: $', int(s * sconeAmount),'.00')
print(teaAmount, 'Tea at $4.00 each: $', int(z * teaAmount),'.00')
print('6% tax: $',(subTotal * .06))
print('---------')
print('Total: $',total)
print('***************************************')
