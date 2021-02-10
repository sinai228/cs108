'''
Model a single particle
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
@edited: Sinai Park(sp46)
'''
import math
from helpers import *

DAMPENING_FACTOR = 0.88


class Particle:
    '''
    Particle models a single particle that may be rendered to a canvas
    '''

    def __init__(self, x = 50, y = 50, velX = 10, velY = 15, radius = 15, color = '#663977'):
        '''
        Constructor
        '''
        self.x = x
        self.y = y
        self.velX = velX
        self.velY = velY
        self.radius = radius
        self.color = color
    
    def render(self, canvas):
        '''This method receives a canvas and uses instance variables to draw a circular representation'''
        canvas.create_oval(self.x - self.radius,
                        self.y - self.radius,
                        self.x + self.radius,
                        self.y + self.radius,
                        fill = self.color)
    
    def move(self, canvas):
        '''This method receives a canvas to animate a particle'''
        
        #negates the velocity(bounce off)
        if (self.x > canvas.winfo_reqheight()) or (self.x - self.radius < 0):
            self.velX = -self.velX
        if (self.y > canvas.winfo_reqwidth()) or (self.y - self.radius < 0):
            self.velY = -self.velY
            
        self.x += self.velX
        self.y += self.velY
        
    #accessor
    def get_x(self):
        '''This method returns the x coordinate of a particle'''
        return self.x
    
    def get_y(self):
        '''This method returns the y coordinate of a particle'''
        return self.y

    def get_radius(self):
        '''This method returns the radius coordinate of a particle'''
        return self.radius
    
    #extra credit 
    def hits(self, other):
        if (self == other):
            # I can't collide with myself.
            return False
        else:
            # Determine if I overlap with the target particle.
            return (self.radius + other.get_radius()) >= distance(self.x, self.y, other.get_x(), other.get_y())
            
     
    def bounce(self, target):
        ''' This method modifies this Particle object's velocities based on its
            collision with the given target particle. It modifies both the magnitude
            and the direction of the velocities based on the interacting magnitude
            and direction of particles. It only changes the velocities of this
            object; an additional call to bounce() on the other particle is required
            to implement a complete bounce interaction.
      
            The collision algorithm is based on a similar algorithm published by K.
            Terzidis, Algorithms for Visual Design.
      
            target  the other particle
         '''
        if self.hits(target):
            angle = math.atan2(target.get_y() - self.y, target.get_x() - self.x)
            targetX = self.x + math.cos(angle) * (self.radius + target.get_radius())
            targetY = self.y + math.sin(angle) * (self.radius + target.get_radius())
            ax = targetX - target.get_x()
            ay = targetY - target.get_y()
            self.velX = (self.velX - ax) * DAMPENING_FACTOR
            self.velY = (self.velY - ay) * DAMPENING_FACTOR
    
        