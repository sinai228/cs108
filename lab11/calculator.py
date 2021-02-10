'''
Provide calculator functionality
Created Fall 2014
updated, Summer, 2015

@author: smn4
@author: kvlinden
'''

class Calculator:
    
    def __init__(self):
        ''' Initialize calculator memory to 0 '''
        self._memory = 0

    def calculate(self, operand1, operator, operand2):
        ''' Perform the specified calculation '''
#         return 1.0
    
        # Implement the calculate function properly.
        if operator == '+':
            result = float(operand1) + float(operand2)
            return result

        if operator == '-':
            result = float(operand1) - float(operand2)
            return result

        if operator == '*':
            result = float(operand1) * float(operand2)
            return result

        if operator == '/':
            if operand2 == 0:
                raise ZeroDivisionError('float division by zero')
            else:
                result = float(operand1) / float(operand2)
                return result

            if operand2 == 0:
                raise ZeroDivisionError('float division by zero')

        if operator != '+':
            if operator != '-':
                if operator != '*':
                    if operator != '/':
                        raise ValueError('Invalid operation: ' + str(operator))
        
        else:
            raise ValueError('could not convert string to float:' + "" + str(operand1) + "") 
               
#         return result
    

        
if __name__ == '__main__':
    # Do a simple test of 1+1. See the more extensive tests in test.py.
    calc = Calculator()
    print(calc.calculate('0', '+', '1'))

