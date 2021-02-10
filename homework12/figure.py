'''This is a figure Class

Created Fall 2018

Homework 12

@author: Sinai Park (sp46)
'''
from random import randint
from lab12.helpers import get_random_color

class Figure:
    '''Figure models a single particle that may be rendered to a canvas'''
    
    #constructor
    def __init__(self, x1 = 50, y1 = 100, x2 = 40, y2 = 20, width = 3, color = "white"):
        '''Constructor'''
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        
        self.width = width
        self.color = color
        
    def render(self, canvas):
        '''This method draws the specific figure on the canvas'''
        canvas.create_line(self.x1, self.y1 , self.x2 , self.y2 , width = self.width , fill = self.color)
        

        