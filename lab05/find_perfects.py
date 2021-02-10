'''
Finding perfect numbers 

Created on Oct. 4, 2018

Lab05

@author: Sinai Park (sp46), Sebene Yi (ssy3), Yeheun Lee (yl55)

'''
#counter
count_perfect = 0

#prompt for user input
#value = int(input('Please enter a positive integer: '))

#if loop
for value in range(2, 10000): 
    
    low = 1
    high = value
    divisors = []
    
    while low < high:
        if value % low == 0:
            high = value // low
            divisors.append(low)
            if high != low:
                divisors.append(high)
        low += 1
                
#exercise 5.1b
#extension to check if value is a perfect number\
    divisors.remove(value)
    list_sum = sum(divisors)
        
    if value == list_sum:
        count_perfect += 1
        
    elif count_perfect == 4:
        print('The number of perfect number in range (2, 10000) were four!')
        break
#description to user
        #if value == list_sum:
            #print('The number you inputed is perfect number')
            #count_perfect += 1
        #else: 
            #print('The number you inputed is not a perfect number. Please try again.'

#exercise 5.1c
