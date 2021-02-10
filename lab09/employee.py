'''This program is to create a data file to calculate about employees.

Created Fall 2018

Lab 09

Sebene Yi (ssy3) and Sinai Park (sp46)
'''

# Importing sys
import sys

class Employee():
    '''This class will be about employees
    Invariant: salary over 20,000'''
    
    #Constructor
    def __init__(self, line = ''):
        '''This method will set up a default employee'''
        if line == '':
            self.first = "Joe"
            self.last = "Biden"
            self.rank = "associate"
            self.salary = 35000
            if int(self.salary) <= 20000:
                print("Invalid employee!", file = sys.stderr)
                sys.exit()
                
        elif line != '':
            strings = line.split()
            self.first = strings[0]
            self.last = strings[1]
            self.rank = strings[2]
            self.salary = int(strings[3])
            if int(self.salary) <= 20000:
                print("Invalid employee!", file = sys.stderr)
                sys.exit()
    
    # String format method
    def __str__(self):
        '''This is the string format for printing'''
        return self.last.capitalize() + ', ' + self.first[0].capitalize() + '.: ' + self.rank + ' ($' + str(self.salary) + ')'
    
    #Accessor
    def get_rank(self):
        '''This accessor get the rank of the employee'''
        return self.rank
    
    def get_salary(self):
        '''This accessor will get the salary of the employee'''
        return self.salary
    
# MAIN CODE -------------------------------------------------------------------------

if __name__ == '__main__':
    t1 = Employee()
    print(t1)

# Test for the new constructor
#if __name__ == '__main__':
    #t2 = Employee('bob looo loser 2000000')
    #print(t2)

# Test for Accessor
#print(t1.get_rank())
#print(t1.get_salary())