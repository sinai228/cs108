'''
Model of a solar system

Created Fall 2014

@author: smn4

@edited: sp46

'''

from sun import Sun
from planet import Planet

class Solar_System:
    
    def __init__(self):
        self._sun = None
        self._planets = []
        
    def add_sun(self, a_sun):
        if isinstance(a_sun, Sun):
            self._sun = a_sun
        else:
            raise TypeError('add_sun(): cannot add ' + str(type(a_sun)) + ' to solar system')
        
    def add_planet(self, a_planet):
        if isinstance(a_planet, Planet):
            self._planets.append(a_planet)
        else:
            raise TypeError('Please redefine the planet you want to add to the list.')
         
    def show_planets(self):
        for a_planet in self._planets:
            print(a_planet)
        
        
        
            
#--------------------------------------------------------------------------------------------------------------------
#MAIN
# 
if __name__ == '__main__':
    
    try:
        ss1 = Solar_System()
        ss1.add_sun(Sun('smallsun', 19, 568211, -37.42872))
        ss1.add_planet(Planet("planetpython", 6, 0.0000001, 4687, "purple"))
    except ValueError as ve:
        print('Dealth with ValueError: ', ve)
        
    try:
        ss2 = Solar_System()
        ss2.add_sun(Sun('smallsun', 253626, 568211, -37.42872))
        ss2.add_planet(Planet("planetpython", 25, -0.0000001, 4687, 'red'))
    except ValueError as ve:
        print('Dealth with ValueError: ', ve)
    
    try:
        ss3 = Solar_System()
        ss3.add_sun(Sun('smallsun', 12, 982, 98))
        ss3.add_planet(Planet("planetpython", 25, 0.0000001, 4687, 'orange'))
    except ValueError as ve:
        print('Dealth with ValueError: ', ve)
    