'''
Created on Sep 6, 2018

Homework 01

@author: Sinai Park (sp46)
'''

#turtle graphics
import turtle

#pen colors
blue = (0, 0, 1)
red = (1, 0, 0)
yellow = (1, 1, 0)
green = (0, 1, 0)
# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it pen.
pen = turtle.Turtle()

# make pen thicker
pen.width(10)
# Create black circle in middle
pen.circle(100)

#move to create blue circle
pen.up()
pen.backward(210)
pen.down()

#create blue circle
pen.pencolor(blue)
pen.circle(100)

#move to create red circle
pen.up()
pen.forward(420)
pen.down()


#create red circle
pen.pencolor(red)
pen.circle(100)

#move to create green circle
pen.up()
pen.backward(110)
pen.right(90)
pen.forward(110)
pen.left(90)
pen.down()

#create green circle
pen.pencolor(green)
pen.circle(100)

#move to create yellow circle
pen.up()
pen.backward(210)
pen.down()

#create green circle
pen.pencolor(yellow)
pen.circle(100)

# Keep the window open until it is clicked.
#window.exitonclick()
