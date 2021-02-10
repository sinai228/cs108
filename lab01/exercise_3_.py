''' A first turtle graphics program
Created Fall 2014
Lab 01
@author: Serita Nelesen (smn4)
'''

# Gain access to the collection of code named "turtle".
import turtle

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it pen.
pen = turtle.Turtle()

# Tell the pen to move forward 250 pixels.
pen.backward(150)

#making the back of the C
pen.left(90)
pen.forward(250)

#top of the C
pen.right(90)
pen.forward(150)

# Space between C and S
pen.up()
pen.forward(200)
pen.down()

#Top of the S
pen.backward(150)
pen.right(90)
pen.forward(125)
pen.left(90)
pen.forward(150)

#Bottom of the S
pen.right(90)
pen.forward(125)
pen.right(90)
pen.forward(150)
# Keep the window open until it is clicked.
window.exitonclick()
