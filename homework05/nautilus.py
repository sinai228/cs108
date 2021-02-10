'''
Drawing multiply-sized versions of the golden spiral

Created on Oct. 6, 2018

Homework05

@author: Sinai Park (sp46)

'''

#import libraries
import turtle
import math

#window turtle
window = turtle.Screen()
turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
pen = turtle.Turtle()

#initialize value of phi
PHI = (1 + math.sqrt(5))/2

#loop for drawing golden spiral
while True:
    choice = input("Would you like to draw a spiral/golden spiral? (Y/N) ")
    if choice == 'n' or choice == 'N':
        break
    elif choice != 'y' and choice != 'Y' and choice != '':
        print('Please enter again')
    else: 
        radius = int(input("Enter the size (radius) of the golden spiral: "))
        color_user = input("Enter the color of your choice: ")
        
        #make circle go clockwise 
        radius = radius * -1
        pen.up()
        pen.goto(-300,-200)
        pen.seth(90)
        pen.down()
        
        #draw until pixel goes to one
        while radius <= -1:
            radius *= (1/(PHI))
            pen.color(color_user)
            pen.circle(radius, 90)

            

#exit window
window.exitonclick()




