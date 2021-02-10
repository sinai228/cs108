'''This is a program to implement fractions
Created Fall 2018
Lab 08
@author: Emma Gordon (ecg25) and Sinai Park (sp46)
'''

import sys

def computeGCD(alha, beta):
    '''(int, int) -> int
    This function finds the greatest common divisor of two integers, using
    Euclid's algorithm '''
    alpha = abs(alpha)
    beta = abs(beta)
    remainder = alpha % beta
    while (remainder != 0):
        alpha = beta
        beta = remainder
        remainder = alpha % beta
    return beta

class Fraction():
    ''' This class will perform fractions '''
    
    #Constructor
    def __init__(self, numerator = 0, denominator = 1):
        ''' This sets up the fraction so that it cannot be
        undefined by making the denominator 1 and the
        numerator 0 so the fraction is 0 (invariant)'''
        if denominator != 0:
            self._numerator = numerator
            self._denominator = denominator
            self.simplify()                   #This simplifies the values provided by the calling program
        else:
            print("Unable to create invalid fraction", file = sys.stderr)
            sys.exit(-1)
            
        
    def __str__(self):
        '''This method receives the string to represent the current state of the fraction object'''
        return str(self._numerator) + '/' + str(self._denominator)
    
    
    #accessor functions
    def get_numerator(self):
        '''This method returns the numerator of the given fraction'''
        return self._numerator
    
    def get_denominator(self):
        '''This method returns the denominator of the given fraction'''
        return self._denominator
        
    #mutator functions
    def simplify(self):
        '''This method receives the fraction and changes it to the lowest common form of the fraction
        and inserts the (-) sign (if present) on the numerator'''
        gcd = computeGCD(self._numerator, self._denominator)
        
        if gcd != 0:
            self._numerator = self._numerator // gcd
            self._denominator = self._denominator // gcd
        if self._denominator < 0:
            self._numerator = self._numerator * -1
            self._denominator = self._denominator * -1
    
    def __mul__(self, other):
        '''This method multiplies and returns the fraction with another fraction'''
        new_fraction = Fraction(self._numerator * other.get_numerator(), self._denominator * other.get_denominator() )  
        return new_fraction
        
        
#------------------------------------------------------------------------------
# MAIN CODE


f1 = Fraction(0, 1)
# f2 = Fraction(3, 0)
f3 = Fraction(2, 4)
f4 = Fraction(4, 10)
f5 = Fraction(5, 3)
f6 = Fraction(-5, -2)
f7 = Fraction(-7, 5)

#tests
print(f1)
# print(f2)
print(f3)                           #test cases for exercise 8.6
print(f4)
print(f5)
print("f1 numerator is", f1.get_numerator())
print("f4 denominator is", f4.get_denominator())
print(f6)                           #test cases for exercise 8.6
print(f7)                           #test cases for exercise 8.6
print("the multiplied fraction of f3 and f5 is", f3 * f5)                      #test cases for exercise 8.7