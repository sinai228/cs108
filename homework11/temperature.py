'''This is a temperature Class

Created Fall 2018

Homework 11

@author: Sinai Park (sp46)
'''

class Temperature:
    '''This class receives a Fahrenheit temperature'''
    #constructor
    def __init__(self, fahrenheit= 0.0):
        '''This method receives a fahrenheit temperature and stores it '''
        if fahrenheit < -459.67:
            raise ValueError('Temperature must be above absolute zero')
        if fahrenheit >= -459.67:
            self._fahrenheit = fahrenheit
        else:
            raise NameError('Please enter a valid number')
    
    #accessor    
    def get_temp(self):
        '''This method returns the Fahrenheit temperature'''
        return self._fahrenheit
    
    def get_celcius(self, f_temperature):
        '''This method returns the equivalent temperature value in Celcius '''
        if ((f_temperature - 32) * (5/9)) <= -273.15:
            raise ValueError('Reached below absolute zero. Enter another temperature value ')
        else:
            return (f_temperature - 32) * (5/9)
      
        
#test cases
if __name__ == '__main__':
    try: 
        temp = Temperature()
        assert temp.get_temp() == 0
    except ValueError as e:
        print(e)
    
    try:
        temp.get_celcius(-456427)
    except ValueError as e:
        print(e)
    
    try:
        temp.get_celcius(8)
    except ValueError as e:
        print(e)
    
    try:
        temp = Temperature(-26782976)
        assert False
    except ValueError as e:
        pass
    
    try:
        temp = Temperature(-459.6)
    except ValueError as e:
        print(e)
    
    try:
        temp = Temperature(-459.7)
    except ValueError as e:
        print(e)
    
    try:
        temp = Temperature(sghsj)
    except NameError as e:
        print(e)
    
    
    
    