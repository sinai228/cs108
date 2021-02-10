'''
Model a sun

Created Fall 2014

@author: smn4

@edited: sp46

'''
import turtle

class Sun:

    def __init__(self, name, rad, m, temp):
        '''This constructor creates a sun, with positive values of radius and meters, but with a temperature greater than absolute zero'''
        self._name = name
        if (rad >= 0) and (m >= 0) and (temp > -273.15):
            self._radius = rad
            self._mass = m
            self._temp = temp
            
            #updated code
            self._x = 0
            self._y = 0
            
            self._turtle = turtle.Turtle()
            self._turtle.up()
            self._turtle.color('yellow') or self._turtle.color('red')
            self._turtle.shape('circle')
            self._turtle.shapesize(self._radius, self._radius)
    
            self._turtle.goto(self._x, self._y)
            
        else: 
            raise ValueError
#        
        
    def get_mass(self):
        return self._mass
    
    def __str__(self):
        return self._name
      
      
#--------------------------------------------------------------------------------------------------------------------
#MAIN
# 
if __name__ == '__main__':  
    
    try:
        s1 = Sun("sunone", 362536, 72327, -3636)
    except ValueError:
        print('Dealt with ValueError: Numeric values must be positive. (temp must be above absolute zero(-273.15 C)) ') 
        
    try:
        s2 = Sun("suntoo", 345, 2, 'name')
    except TypeError: 
        print('Dealt with TypeError: Please enter an integer')
        
    try:
        s3 = Sun("suntree", 345, -.00000002, 2342)
    except ValueError:
        print('Dealt with ValueError: Numeric values must be positive. (temp must be above absolute zero(-273.15 C)) ')  
        
        
        
    #set up window
    window = turtle.Screen()
    turtle.setup(width = 1000, height = 600, startx = 100, starty = 100)
    
    
#Keep the window open until it is clicked
    window.exitonclick()                
                  
    