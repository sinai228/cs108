'''Overlap Circle
September 27, 2018
Lab 04
@author: Sinai Park (sp46)
'''

import turtle

#user inputs of center coordinates of circles one and two
center_coord_x = int(input('please enter the x coordinates for circle 1: '))
center_coord_y = int(input('please enter the y coordinates for circle 1: '))
center_coord_x2 = int(input('please enter the x coordinates for circle 2: '))
center_coord_y2 = int(input('please enter the y coordinates for circle 2: '))

#set center coordinates as tuples
cc_1 = (center_coord_x, center_coord_y)
cc_2 = (center_coord_x2, center_coord_y2)

#user input of radius of both circle 1 and 2
radius1 = int(input('Please enter radius of circle 1: '))
radius2 = int(input('Please enter radius of circle 2: '))

#window turtle
window = turtle.Screen()

pen = turtle.Turtle()

#draw circle one and two
pen.up()
pen.goto(cc_1)
pen.down()
pen.circle(radius1)
pen.up()
pen.goto(cc_2)
pen.down()
pen.circle(radius2)

#if and else statement
if pen.distance(cc_1, cc_2) + min(radius1, radius2) < max(radius1, radius2):
    if max(radius1, radius2) == radius1:
        pen.write('Circles 1 contains circle 2')
    else:
        pen.write('Circles 2 contains circle 1')
    
elif pen.distance(cc_1, cc_2) > (radius1 + radius2):
    pen.write('Circles are disjoint')   
else:
    pen.write('Circle 1 and 2 overlap')

pen.ht()

#exit the window 
window.exitonclick()