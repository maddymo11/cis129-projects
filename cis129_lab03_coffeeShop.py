#Author: Maddy Simonds
#this program is an interactive text-based coffee shop simulator
#x represents cost of coffees
#y represents cost of muffins
x = 5
y = 4
coffeeAmount = int(input('Number of coffees bought?'))
muffinAmount = int(input('Number of muffins bought?')) 
subTotal = int((x * coffeeAmount) + (y * muffinAmount))
#function adds the total cost of both variables
#subTotal represents total before tax
total = subTotal + (subTotal * .06) 
#function adds subTotal and tax to make the final total
print('***************************************')
print('My Coffee and Muffin Shop')
print('Number of coffees bought?')
print(coffeeAmount)
print('Number of muffins bought?')
print(muffinAmount)
print('***************************************\n\n***************************************')
print('My Coffee and Muffin Shop Receipt')
print(coffeeAmount, 'at $5.00 each: $',int(x * coffeeAmount),'.00')
print(muffinAmount, 'at $4.00 each: $',int(y * muffinAmount),'.00')
print('6% tax: $',(subTotal * .06))
print('---------')
print('Total: $',total)
print('***************************************')
