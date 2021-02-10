'''
Making a program that imports rectangle module, 
read contents of another text file and draws on turtle

Created on Nov 1, 2018

Homework 09

@author: Sinai Park (sp46)
'''

#open a file rectangles to write
with open('rectangles.txt', 'w') as file:
#write a set of hard-coded rectanvle specifications to the file
    file.write('100 -200 60 30 black' + '\n' + '400 200 10 40 red' + '\n' + '300 50 100 40 purple')

