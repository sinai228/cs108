'''This is a program to incorporate TKinter and Calculator

Created Fall 2018

Lab 11

@author: Sinai Park (sp46)
'''

from tkinter import *
from calculator import *


class Gui:
    '''This will create the GUI application class'''
    
    #Constructor
    def __init__(self, window):
        '''This method will open up a window that calculates two input values and the function selected by the user '''
        #creating an instance variable
        self.calc = Calculator()        
        
        #entry for first number
        self.input1 = StringVar()
        input1_label = Label(window, text = "Input 1:")
        input1_label.grid(row = 0, column = 0, sticky = E)
        input1_entry = Entry(window,  textvariable = self.input1, width = 6)
        input1_entry.grid(row = 0, column = 1, sticky = W)
        
        #entry for second number
        self.input2 = StringVar()
        input2_label = Label(window, text = "Input 2:")
        input2_label.grid(row = 1, column = 0, sticky = E)
        input2_entry = Entry(window, textvariable = self.input2, width = 6)
        input2_entry.grid(row = 1, column = 1, sticky = W)
    
        #adding radio buttons
        operator_frame = Frame(window)
        operator_frame.grid(row=2, column=0, columnspan=2)
        self.operator = StringVar()
        self.operator.set('+')
        
        #creating button for addition operation
        add_button = Radiobutton(operator_frame, text = "+", variable = self.operator, value = '+')
        add_button.pack(side=LEFT)
        
        #creating button for subtraction operation
        add_button = Radiobutton(operator_frame, text = "-", variable = self.operator, value = '-')
        add_button.pack(side=LEFT)
        
        #creating button for multiplication operation
        add_button = Radiobutton(operator_frame, text = "*", variable = self.operator, value = '*')
        add_button.pack(side=LEFT)
    
        #creating button for division operation
        add_button = Radiobutton(operator_frame, text = "/", variable = self.operator, value = '/')
        add_button.pack(side=LEFT)
        
        #creating button to perform calculation
        add_button = Button(window, text = 'Calculate', command = self.do_calculation)
        add_button.grid(row=3, column=0, sticky=E) 
        
        #adding a label to the window
        result_label = Label(window, text = "Result:")
        result_label.grid(row = 3, column = 1, sticky = W)
        
        #creating label that matches self.result (answer)
        self.result = StringVar()
        self.result_label = Label(window, textvariable = self.result, width=6)
        self.result_label.grid(row=3, column=2, columnspan=6, sticky=W)
        
        #creating a message label
        self._message = StringVar()
        self._message.set('Welcome to the calculating world!')
        message_label = Label(window, textvariable = self._message, width=40)
        message_label.grid(row=4, column=0, columnspan=3)
        
        
        
    def do_calculation(self):
        '''This method is a command function for the calculator button to callback once the user presses the button'''
        try:
            result = self.calc.calculate(self.input1.get(), self.operator.get(), self.input2.get())
#             print(result)
            self.result.set(result)

        except ZeroDivisionError as zde:
            self._message.set('Enter a valid denominator: \n ' + str(zde))
        except ValueError as ve:
            self._message.set('Enter a valid value: \n'+ str(ve))
        else: 
            self._message.set('Welcome to the calculating world!')
        
    
#main test code
if __name__ == '__main__':
    root = Tk()
    root.title('Calculator')
    app = Gui(root)
    root.mainloop()