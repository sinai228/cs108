'''
slice

Created on Sep 20, 2018

Lab 3

@author: Sinai Park (sp46), Gaby Pineda (gjp3), Yeheun Lee (yl55)
'''
#store first name
first_name = input('Please enter your first name:')

#tore last name
last_name = input('Please enter your last name:')

#store student number
stu_number = input('Please enter your student number:')

#slice up numbers and letters to make loginid
login = (first_name[0] + last_name[0:5] + stu_number[-2:])

#lowercase of login id
login.lower()

#print login id
print(login)
