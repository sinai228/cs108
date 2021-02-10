'''
Making a program that imports rectangle module, 
read contents of another text file and draws on turtle

Created on Nov 1, 2018

Homework 09

@author: Sinai Park (sp46)
'''
#import systems
import sys
import turtle
import math

from rectangle import Rectangle

#set up Turtle window
# window = turtle.Screen()
# turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
# pen = turtle.Turtle()

#creating rectangels list
rectangles = []

#opening up file text from input user
try:
    f = open(input("Please enter the file name: "))
except FileNotFoundError:
    print('File was not found')


#creating a list of rectangles listed in the specific file
try: 
    for line in f:
        new_rectangle = line.strip().split()
#         print(info)
#         new_r = Rectangle((int(info[0]), int(info[1])), int(info[2]), int(info[3]), str(info[4]))
        rectangles.append(new_rectangle) 
#         new_r.render(pen)   
    print(rectangles)
except NameError as ne:
    print('Dealt with NameError: ', ne)
except TypeError as te:
    print('Dealt with NameError: ', te)

#exit window on click
# window.exitonclick() 