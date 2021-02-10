'''
Models a  problem

Created Fall 2014

Lab 13

@author: smn4
@edit: Sinai Park(sp46)
'''

#new class
class Problem:
    '''A bigger problem that includes different types of problems'''
    def __init__(self, q = ''):
        '''constructs and receives and string and sores it'''
        self.text = q
    
    #accessor
    def get_text(self):
        '''Returns the text'''
        return self.text