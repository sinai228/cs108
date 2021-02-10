'''
Model a planet

Created Fall 2018

@author: smn4

@edited: Sinai Park(sp46)
'''
import turtle



class Planet:
    
    def __init__(self, name, rad, m, dist, color):
        '''This constructor creates a planet name, with positive values of radius, meters, and distance'''
        self._name = name
        if (rad >= 0) and (m >= 0) and (dist >= 0):
            self._radius = rad
            self._mass = m
            self._distance = dist
            self._color = color
            
            #updated variables
            self._x = dist
            self._y = 0
            
            self._turtle = turtle.Turtle()
            self._turtle.up()
            self._turtle.color(self._color)
            self._turtle.shape('circle')
            self._turtle.shapesize(self._radius, self._radius)
    
            self._turtle.goto(self._x, self._y)
            
            
        else: 
            raise ValueError("A planetary numeric value is invalid")
                                
    def get_name(self):
        return self._name
    
    def get_radius(self):
        return self._radius
    
    def get_mass(self):
        return self._mass
    
    def get_distance(self):
        return self._distance
    
    def set_name(self, newname):
        self._name = newname
    
    def __str__(self):
        return self._name
    
    
    
#--------------------------------------------------------------------------------------------------------------------
#MAIN
# 
if __name__ == '__main__':
#     
    try:
        p1 = Planet("planetearth", 253,  25, 7332, 'red')
    except ValueError as ve:
        print("Dealt with ValueError: ", ve)
            
    try:
        p2 = Planet("pluto", 0.00001, 295, 63, 'black')
    except ValueError as ve:
        print("Dealt with ValueError: ", ve)
        
    try:
        p3 = Planet("not valid", 236, 234, -307637692706235, 'yellow')
    except ValueError as ve:
        print("Dealt with ValueError: ", ve)
            
    try:
        p4 = Planet("invalid", 23, -.000002, 123, 'purple')
    except ValueError as ve:
        print("Dealt with ValueError: ", ve)
        
    try:
        p5 = Planet("asdfhjk", -253,  25, 7332, 'blue')
    except ValueError as ve:
        print("Dealt with ValueError: ", ve)

#     print(p1)
    
    window = turtle.Screen()
    turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
    
    

#Keep the window open until it is clicked
    window.exitonclick()                
            
