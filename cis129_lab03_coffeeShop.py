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
#if statements will correctly pluralize item amounts on receipt
if coffeeAmount == 1:
  print(coffeeAmount, 'Coffee at $5.00 each: $',int(x * coffeeAmount),'.00')
if coffeeAmount > 1:
  print(coffeeAmount, 'Coffees at $5.00 each: $',int(x * coffeeAmount),'.00')
if muffinAmount == 1:
  print(muffinAmount, 'Muffin at $4.00 each: $',int(y * muffinAmount),'.00')
if muffinAmount > 1:
  print(muffinAmount, 'Muffins at $4.00 each: $',int(y * muffinAmount),'.00')
if sconeAmount == 1:
  print(sconeAmount, 'Scone at $4.00 each: $', int(s * sconeAmount),'.00')
if sconeAmount > 1:
  print(sconeAmount, 'Scones at $4.00 each: $', int(s * sconeAmount),'.00')
if teaAmount == 1:
  print(teaAmount, 'Tea at $4.00 each: $', int(z * teaAmount),'.00')
if teaAmount > 1:
  print(teaAmount, 'Teas at $4.00 each: $', int(z * teaAmount),'.00')
print('6% tax: $',(subTotal * .06))
print('---------')
print('Total: $',total)
print('***************************************')
print('Thank you for visiting My Coffee and Muffin Shop! :)')
print('We hope to see you again soon! (っ◔◡◔)っ ♥')
print('***************************************')
