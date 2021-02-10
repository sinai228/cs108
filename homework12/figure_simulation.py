'''This is a program to incorporate TKinter and figure

Created Fall 2018

Homework 12

@author: Sinai Park (sp46)
'''

from tkinter import *
from figure import *


class FigureSimulation:
    ''' Creates particle simulator '''
    
    def __init__(self, window):
        ''' Construct the figure simulator GUI '''
        
        self.window = window
        self.window.protocol('WM_DELETE_WINDOW', self.safe_exit)
        self.width = 500
        self.canvas = Canvas(self.window, bg='black', width=self.width, height=self.width)
        self.canvas.pack()
        self.terminated = False
        
        add_button = Button(self.window, text = "Clear Canvas", command = self.clear_canvas)
        add_button.pack()
        
        add_button = Button(self.window, text = "Quit", command = self.safe_exit)
        add_button.pack()
        
        self.canvas.bind('<Button-1>', self.clear_canvas_mouse)
       
        while self.terminated == False:
            self.add_line()
            self.canvas.after(50)
            self.canvas.update()
        
            
    def safe_exit(self):
        ''' Turn off the event loop before closing the GUI '''
        self.terminated = True
        self.window.destroy()
 
    def clear_canvas_mouse(self, event):
        '''This method deletes the whole canvas once the mouse is clicked'''
        self.canvas.delete(ALL)
    
    def clear_canvas(self):
        '''This method deletes the whole canvas once the button is clicked'''
        self.canvas.delete(ALL)
        
    def add_line(self):
        '''This method continues to render random figures on the canvas'''
        line = Figure(randint(0, 500), randint(0, 500), randint(0, 500), randint(0, 500) ,  width = randint(0, 10) , color = get_random_color())
        line.render(self.canvas)
        
if __name__ == '__main__':
    root = Tk()
    root.title('Figure Simulation(homework12)')    
    app = FigureSimulation(root)
    root.mainloop()
