'''
Drawing Spirographs

Created on Oct. 4, 2018

Lab05

@author: Sinai Park (sp46), Sebene Yi (ssy3), Yeheun Lee (yl55)

'''
#import libraries
import turtle
import math


#window turtle
window = turtle.Screen()
pen = turtle.Turtle()


#initialize
pen.up()           

while True:
    choice = input('Would you like to draw a spirograph? (y/n)')
    if choice == 'n' or choice == 'N':
        break
    elif choice != 'y' and choice != 'Y' and choice != '':
        print('Please answer again')
    else:
        time = 0.0
        mov_rad = float(input('Enter moving radius:'))
        fix_rad = float(input('Enter fixed radius:'))
        pen_offset = float(input('Enter pen offset:'))
        color = str(input('Enter color: '))
        
        #equation for spirograph
        x = (fix_rad + mov_rad) * math.cos(time) + pen_offset * math.cos(((fix_rad + mov_rad) * time) / mov_rad)
        
        y = (fix_rad + mov_rad) * math.sin(time) + pen_offset * math.sin(((fix_rad + mov_rad) * time) / mov_rad)
        
        pen.up()
        pen.color(color)
        pen.speed('fastest')
        pen.goto(x,y)
        pen.down()

        while time < 100:
            time += 0.1
            x = (fix_rad + mov_rad) * math.cos(time) + pen_offset * math.cos(((fix_rad + mov_rad) * time) / mov_rad)
        
            y = (fix_rad + mov_rad) * math.sin(time) + pen_offset * math.sin(((fix_rad + mov_rad) * time) / mov_rad)
            
            pen.speed('fastest')
            pen.goto(x,y)
            pen.pendown()
       

window.exitonclick()