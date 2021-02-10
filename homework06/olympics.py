'''
Making a figure of my own design (olympics)

Created on Oct 10, 2018

Homework 06

@author: Sinai Park (sp46)
'''

#turtle graphics
import turtle

#window turtle
window = turtle.Screen()
turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
pen = turtle.Turtle()

def olympics(marker, x, y, scale_factor):
    '''this function creates an olympics logo figure'''
    RAD = scale_factor
    marker.width(scale_factor*.15)
    marker.speed("fastest")
    
# Create black circle in middle
    marker.goto(x,y)
    marker.pencolor("black")
    marker.down()
    marker.circle(RAD)
    
#move to create blue circle
    marker.up()
    marker.goto(x-(RAD*2.1), y)
    marker.down()
    marker.color("blue")
    marker.circle(RAD)
    
#move to create red circle
    marker.up()
    marker.goto(x+(RAD*2.1), y)
    marker.down()
    marker.pencolor("red")
    marker.circle(RAD)

#move to create green circle
    marker.up()
    marker.goto(x+RAD, y-RAD)
    marker.down()
    marker.pencolor("green")
    marker.circle(RAD)
 
#move to create yellow circle
    marker.up()
    marker.goto(x-RAD, y-RAD)
    marker.down()
    marker.pencolor("yellow")
    marker.circle(RAD)
    marker.up()

def test_olympics():
    olympics(pen, 0, 0, 100)
    olympics(pen, -200, 50, 30)
    olympics(pen, -200, -200, 50)

test_olympics()

# Keep the window open until it is clicked.
window.exitonclick()
