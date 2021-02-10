'''
Created on Sep 13, 2018

Homework 02

@author: Sinai Park (sp46)
'''
# Gain access to the collection of code named "turtle".
import turtle

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it pen.
pen = turtle.Turtle()

#set unit
unit = int(input('Please input the value of the unit: '))

#create the flag boundary
pen.forward(unit*3)
pen.left(90)
pen.forward(unit*2)
pen.left(90)
pen.forward(unit*3)
pen.left(90)
pen.forward(unit*2)
pen.left(90)

#move pen to draw circle
pen.up()
pen.forward(unit*1.5)
pen.left(90)
pen.forward((unit*2)*(1/5))
pen.right(90)

#draw the red filled circle
pen.down()
pen.pencolor(1, 0, 0)
pen.fillcolor(1, 0, 0)
pen.begin_fill()
pen.circle((unit*2)*(3/10))
pen.end_fill()


window.exitonclick()