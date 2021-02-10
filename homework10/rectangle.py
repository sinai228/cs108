'''
Making a class that represents rectangle objects

Created on Fall 2018

Homework 10

@author: Sinai Park (sp46)
'''

#import
import sys
import turtle
import math

#window turtle
if __name__ == '__main__':
    window = turtle.Screen()
    turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
    pen = turtle.Turtle()

def distance(p0, p1):
    return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)
def distance_y(p0, p1):
    return math.sqrt(max(p0[1], p1[1]) - min(p0[1], p1[1]))


class Rectangle():
    '''This class creates a rectangle'''
    #Constructor
    def __init__(self, corner = (0,0), width = 50, height = 50, color = "black" ):
        '''This method sets up a default triangle '''
        if (width <= 0) and (height <= 0):
            raise ValueError("Unable to create a rectangle (enter a positive height and width)")
        else:
            self._corner = corner
            self._width = width
            self._height = height
            self._color = color
            
    #Printing     
    def __str__(self):
        '''This method prints the internal state of the rectangle'''
        return "The rectangle starts at an upper left corner of" + str(self._corner) + ", with a width of " + str(self._width) + ", height of " + str(self._height) + ", and the color " + str(self._color)
        
    #Accessors
    def get_area(self):
        '''This returns the area of a given rectangle '''
        return (self._height * self._width)
    
    def get_perimeter(self):
        '''This returns the perimeter of a given rectangle '''
        return (self._width * 2 + self._height * 2)
    
    def get_corner(self):
        '''This returns the corner of a given rectangle'''
        return self._corner
    
    def get_width(self):
        '''This returns the width of a given rectangle'''
        return self._width

    def get_height(self):
        '''This returns the height of a given rectangle'''
        return self._height

    #Mutators
    def modify_width(self, delta):
        '''This method modifies the width of a given rectangle'''
        self._width = self._width + delta
        if self._width > 0:
            self._width = self._width + delta
        else:
            raise ValueError('Unable to modify width. Enter another value.')   
            
    def modify_height(self, delta):
        '''This method modifies the height of a given rectangle'''
        self._height = self._height + delta
        if self._height > 0:
            return True
        else:
            raise ValueError('Unable to modify height. Enter another value')   
    
    #Overlaps
    def overlaps(self, other_rec):
        '''This function receives another rectangle and compares it with the original one to see if the two overlap in any way'''
        corner1 = other_rec.get_corner()
        corner2 = self.get_corner()
        width1 = self.get_width()
        width2 = other_rec.get_width()
        height1 = self.get_height()
        height2 = other_rec.get_height()
        if (distance(corner1, corner2) <= max (width1, width2)) and (distance_y(corner1, corner2) <= max (height1, height2)):
            return "The two rectangles overlap"
        else:
            return "The two rectangles are disjoint"
        
    #Render
    def render(self, Turtle):
        '''This method calls Turtle to draw a given rectangle'''
        pen.up()
        pen.pencolor(self._color)
        pen.goto(self._corner)
        pen.seth(0)
        pen.down()
        pen.forward(self._width)
        pen.right(90)
        pen.forward(self._height)
        pen.right(90)
        pen.forward(self._width)
        pen.right(90)
        pen.forward(self._height)
        
        
        
#------------------------------------------------------------------------------
# MAIN CODE

#for overlapping rectangles
r6 = Rectangle((5,230), 100, 50, "black")
r7 = Rectangle((50, 200), 50, 20, "red")


#test cases of rectangles

if __name__ == '__main__':
    try:
        r6.modify_height(-245627)
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
    except TypeError as te:
        print('Dealt with TypeError: ', te)
        
    try:
        r6.modify_height(sfgjsfja)
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
    except NameError as ne:
        print('Dealt with NameError: ', ne)

    try:
        r1 = Rectangle()
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
        
    try:
        r2 = Rectangle((500, 100), 30, 70, "blue" )
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
     
    try:
        r3 = Rectangle((100, 400), 30, 70, "red")
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
        
    try:
        r4 = Rectangle((36, 26), rwsthysr, 3637, "yellow")
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
    except NameError as ne:
        print('Dealt with NameError: ', ne)

    try:
        r4 = Rectangle((36, 26), -36, "yellow")
    except ValueError as ve:
        print('Dealt with ValueError: ', ve)
    except TypeError as te:
        print('Dealt with TypeError: ', te)
    
#     print(r1)
#         
#     print(r3)
#      
#     try:
#         print("The area of r4 is", r4.get_area(), "units squared")
#         print("The perimeter of r4 is", r4.get_perimeter(), "units")
#     except NameError as ne:
#         print('Dealt with NameError: ', ne)
#         
#          
# # r5 = Rectangle((100, 400), -30, -70, "yellow")
# # print(r5)
# # print(r1.render(pen))
# # print(r1.modify_height(-60))
# 
# 
#     print(r1.modify_height(50))
#  
# #overlapping rectangles
# 
#     r6.render(turtle)
#      
#     r7.render(turtle)
#      
#     print(r6.overlaps(r7))
#  
# #exit the window 
# 
#     window.exitonclick()