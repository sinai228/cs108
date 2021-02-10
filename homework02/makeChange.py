'''
Created on Sep 13, 2018

Homework 02

@author: Sinai Park (sp46)
'''

#create user input value cost
cost = int(input('Please enter the charged amount for the transaction: '))

#create user input value paid
paid = int(input('Please enter the amount paid: '))

#create and print the value, change
change = paid - cost 
print('Change is $',change, ':' '\n')


#store tens digit 
tens_digit = (change // 10)

#store ones digit 
ones_digit = (change%10)

#twenty dollar bill changes
twenty_bill = tens_digit // 2
 
#ten dollar bill changes
ten_bill = tens_digit % 2

#five dollar bill changes
five_bill = ones_digit // 5

#one dollar bill changes
one_bill = ones_digit % 5

#print the min number of bills
print(twenty_bill,  '20 dollar bill(s)')

print(ten_bill,  '10 dollar bill(s)')

print(five_bill,  '5 dollar bill(s)')

print(one_bill,  '1 dollar bill(s)')
