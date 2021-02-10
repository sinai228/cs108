'''
Driver of Solar System

Created on Nov 8, 2018

@author: sp46
'''


import turtle
from sun import Sun
from planet import Planet
from solar_system import Solar_System

#create turtle window
window = turtle.Screen()
window.setworldcoordinates(-1, -1, 1, 1)

ss = Solar_System() 
ss.add_sun(Sun("SUN", 8.5, 1000, 5800))
ss.add_planet(Planet("EARTH", .475, 5000, 0.6, 'blue'))



#user input values

try:
    name = str(input("Please enter the name of the planet: "))
    rad = float(input("Please enter a valid integer for the radius of planet: "))
    m = float(input("Please enter a valid integer for the mass of planet: "))
    dist = float(input("Please enter a valid integer for the distance of planet from the sun: "))
    color = str(input("Please enter a preferred color for planet: "))
    
    ss_test = Solar_System()
    ss_test.add_planet(Planet(name, rad, m, dist, color))
    print(ss_test)
    
except ValueError:
    print("Please enter a valid user input: ")
except NameError:
    print("Please enter a valid user input: ")
    


#Keep the window open until it is clicked
window.exitonclick()                
            