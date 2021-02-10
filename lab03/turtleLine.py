'''
User described line

Created on Sep 20, 2018

Lab 3

@author: Sinai Park (sp46), Gaby Pineda (gjp3), Yeheun Lee (yl55)
'''

#Gain access to the collection of code named "turtle".
import turtle
import math

x1 = float(input('Please enter x1 value: '))
y1= float(input('Please enter y1 value: '))
           
point1 = (x1, y1)
           
print(point1)


x2 = float(input('Please enter x2 value: '))
y2= float(input('Please enter y2 value: '))
           
point2 = (x2, y2)
           
print(point2)

# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it pen.
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

#move pen to point1
pen.goto(point1)

pen.pendown()

#describe coordinate pt1
pen.write("p1" + str(point1), font=("Arial", 20,"italic"))

#draw line to point2 and describe coordinate pt2
pen.goto(point2)

pen.write("p2" + str(point2), font=("Arial", 20,"italic"))

window.exitonclick()