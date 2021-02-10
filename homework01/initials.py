'''
Created on Sep 6, 2018

Homework 01

@author: Sinai Park (sp46)
'''


# gain access
import turtle

#initials: sp

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it pen.
pen = turtle.Turtle()

#move pen furthur up and left
pen.up()
pen.left(90)
pen.forward(150)
pen.right(90)
pen.down()

#create s
pen.backward(150)
pen.right(90)
pen.forward(125)
pen.left(90)
pen.forward(150)
pen.right(90)
pen.forward(125)
pen.right(90)
pen.forward(150)

#ready to draw p
pen.up()
pen.backward(200)
pen.down()

#create p

pen.right(90)
pen.forward(250)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(125)
pen.right(90)
pen.forward(150)

#make turtle screen stay until click
window.exitonclick()
