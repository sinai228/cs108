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
pen.forward(250)

# Tell pen to turn right 45 angles. 
pen.right(145)

# Tell pen to create second line
pen.forward(250)

# Tell pen to turn right 45 angles. 
pen.right(143)

# Tell pen to create third line
pen.forward(250)

# Tell pen to turn right 45 angles. 
pen.right(143)

# Tell pen to create fourth line
pen.forward(250)

# Tell pen to turn right 45 angles. 
pen.right(145)

# Tell pen to create final line
pen.forward(250)

# Keep the window open until it is clicked.
window.exitonclick()