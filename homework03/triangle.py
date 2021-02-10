'''
Triangle 

Created on Sep 20, 2018

Homework03

@author: Sinai Park (sp46)
'''


#Gain access to the collection of code named "turtle".
import turtle
import math

#store coordinate 1 in tuple
x1 = int(input('Please enter x1 value: '))
y1= int(input('Please enter y1 value: '))     
p1 = (x1, y1)       

#store coordinate 2 in tuple
x2 = int(input('Please enter x2 value: '))
y2= int(input('Please enter y2 value: '))
p2 = (x2, y2)

#store coordinate 3 in tuple
x3 = int(input('Please enter x3 value: '))
y3 = int(input('Please enter y3 value: '))      
p3 = (x3, y3)



# Give the name "window" to the screen where the turtle will appear.
window = turtle.Screen()

# Create a turtle and name it pen.
pen = turtle.Turtle()
pen.hideturtle()


#move pen to point1 and show pen
pen.up()
pen.goto(p1)
pen.down()

pen.goto(p2)
pen.goto(p3)
pen.goto(p1)

pen.goto(p3)

#determine min max value of y and x
list_y = [y1, y2, y3]
list_x = [x1, x2, x3]


max_y = max(list_y)
min_y = min(list_y)

min_x = min(list_x)

p4 = (x3, min_y)

#draw a perpendicular line
pen.goto(p4)
pen.up()


#compute side lengths and perimeter
s1 =  math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
s2 =  math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
s3 =  math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2) 

perimeter = s1 + s2 +s3


#compute area
s4 = math.sqrt((y3 - min_y) ** 2) 
area = 1/2*(s1*s4)

#write the points, perimeter, and area
left = ((min_x - 500), max_y)
pen.goto(left)
pen.write('Coordinate points: ' + str(p1 )  + str(p2 ) + str(p3 ) + '\n'
           + 'Perimeter of Triangle:'+ str(perimeter) + ' pixels' + '\n' \
           + 'Area of Triangle: ' + str(area) + ' pixels squared', \
            align = "left", font=("Arial", 12,"normal"))



window.exitonclick()