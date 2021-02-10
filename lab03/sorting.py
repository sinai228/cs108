'''
Basic lists
Created on Sep 20, 2018

Lab 3

@author: Sinai Park (sp46), Gaby Pineda (gjp3), Yeheun Lee (yl55)
'''


#store four values
first_num = int(input('Please enter first number: '))
second_num = int(input('Please enter second number: '))
third_num = int(input('Please enter third number: '))
fourth_num = int(input('Please enter fourth number: '))

list1 = [first_num, second_num, third_num, fourth_num]

print(list1)
print(min(list1))

list2 = []

#loop until minimum number goes in the front
while len(list1) > 0:
    list2.append(min(list1))
    list1.remove(min(list1)) 
    

print(list2)
