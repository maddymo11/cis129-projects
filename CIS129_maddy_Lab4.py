# maddy simonds
# 9-23-24 CIS129 lab 4
# program determines bonus amount for a store and its employees dependent on monthly sale amount and sales increase
# declare local variables
monthlySales = 0 # monthly sales amount
storeAmount = 0 # store bonus amount
empAmount = 0 # employee bonus amount
salesIncrease = 0 # percent of sales increase
prompt = str # prompt will be a string literal
# this code gets the monthy sale amount
monthlySales = float(input('Please enter monthly sales $')) # this code gets monthly sales
#this code will determine storeAmount bonus
if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else:
    storeAmount = 0
# this will get the percentage of sales increase
salesIncrease = float(input('Please enter percentage of sales increase: '))
salesIncrease = salesIncrease / 100
# this will determine the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0
# this will print the bonus info
print ('The store bonus amount is $', storeAmount)
print ('The employee bonus amount is $', empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print ('Congrats! You have reached the highest bonus amounts possible! ')