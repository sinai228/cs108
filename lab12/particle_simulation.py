'''
GUI controller for a particle simulation
Created Fall 2014
Updated Summer, 2015

@author: smn4
@author: kvlinden
'''

from tkinter import *
import random 
from particle import Particle
from helpers import *


class ParticleSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the particle simulator GUI '''
        #instance variable as default particle
#         self.p1 = Particle()
        self.p_list = []
        
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 400
        self.canvas = Canvas(self.window, bg='black', width=self.width, height=self.width)
        self.canvas.pack()
        self.terminated = False
        
        add_button = Button(self.window, text = "Add particle", command = self.add_particle)
        add_button.pack()
        
        self.canvas.bind('<Button-1>', self.check_remove_particle)

        #ask particle to render itself on canvas
#         self.p1.render(self.canvas)

        #updated code
        while self.terminated == False:
            self.canvas.delete(ALL)
#             self.p1.move(self.canvas)
#             self.p1.render(self.canvas)
            #update code
            for p in self.p_list:
                p.move(self.canvas)
                p.render(self.canvas)
                for p2 in self.p_list:
                    p.bounce(p2)
            self.canvas.after(50)
            self.canvas.update()
            
    def add_particle(self):     
        '''This method adds particles to the list'''   
        add_particle = Particle(randint(-25, self.width -25), randint(-25, self.width - 25), randint(-25,25), randint(-25,25),randint(5,25), color = get_random_color())
        self.p_list.append(add_particle)
        
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()

    def check_remove_particle(self, event):
        '''This method allows a click of the first button to remove a particle'''
        copy_list = self.p_list[:]
        for p in copy_list:
            if (distance(event.x, event.y, p.get_x(), p.get_y()) < p.get_radius()):
                self.p_list.remove(p)
                
    
if __name__ == '__main__':
    root = Tk()
    root.title('Particle Simulation')    
    app = ParticleSimulation(root)
    root.mainloop()
