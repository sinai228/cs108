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

from rectangle_homework09 import Rectangle

#set up Turtle window
window = turtle.Screen()
turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
pen = turtle.Turtle()
    
rectangles = []
#opening up file text
with open('rectangles.txt', 'r') as file:
    for line in file:
        info = line.split()
#         print(info)
        new_r = Rectangle((int(info[0]), int(info[1])), int(info[2]), int(info[3]), str(info[4]))
        rectangles.append(new_r) 
        new_r.render(pen)   
    print(rectangles)
    
window.exitonclick() 