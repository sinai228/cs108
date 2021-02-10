'''This is a program to incorporate TKinter and Temperature

Created Fall 2018

Homework 11

@author: Sinai Park (sp46)
'''
#import
from temperature import *
from tkinter import *

class Gui:
    '''This will create the GUI application class'''
    #Constructor
    def __init__(self, window):
        '''This method will open up a window that converts a fahrenheit temperature to celcius '''
        #creating an instance variable
        self.temp = Temperature()  
        
        #creating label
        temp_label = Label(window, text = 'Temperature (in F):')
        temp_label.grid(row = 0, column = 0, sticky = E)
        
        #creating entry
        self._ftemp = IntVar()
        temp_entry = Entry(window, textvariable = self._ftemp, width = 5)
        temp_entry.grid(row = 0, column = 1, sticky = W)
        
        #creating conversion button
        convert_button = Button(window, text = 'Convert to Celcius', command = self.convert_celcius)
        convert_button.grid(row = 1, column = 0, sticky = E)
        
        #creating conversion label
        self._ctemp = IntVar()
        c_label = Label(window, textvariable = self._ctemp)   
        c_label.grid(row = 1, column = 1, sticky = W)
        
        #creating message label
        self._message = StringVar()
        self._message.set('Welcome to Temperature Convertor!')
        message_label = Label(window, textvariable = self._message, width = 50)
        message_label.grid(row = 2, column = 0, columnspan = 2)
            
       
    def convert_celcius(self):
        '''This method is a command function for the conversion button to callback once the user presses the button'''        
        try: 
            celcius = self.temp.get_celcius(self._ftemp.get()) 
            self._ctemp.set(celcius) 
        except ValueError as e:
            self._message.set(e)
        except NameError as e:
            self._message.set(e)
        except TclError as e:
            self._message.set(e)
        else:
            self._message.set('Welcome to Temperature Convertor!')
        
 #main test code
if __name__ == '__main__':
    root = Tk()
    root.title('Temperature Converter')
    app = Gui(root)
    root.mainloop()