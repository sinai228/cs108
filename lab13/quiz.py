'''
Provides quiz functionality

Created Fall 2014

Lab 13

@author: smn4
@edit: Sinai Park(sp46)

'''

from shortAnswer import ShortAnswer
from FillInTheBlank import FillInTheBlank
from TrueFalse import TrueFalse

import random

class Quiz:
    ''' Build a simple quiz game '''
    
    def __init__(self):
        ''' Construct a quiz object with a list of question objects '''
        
        self.problems = []
        self.problems.append(ShortAnswer('Where were the olympics held in 1956', 'Melbourne'))
        self.problems.append(ShortAnswer('What is the hottest recorded temperature in the United States', '134'))
        self.problems.append(ShortAnswer('What is the best snack in the world?', 'Chocolate'))
        self.problems.append(FillInTheBlank('There are ____ number of students in CS 108 Lab A.', '33'))
        self.problems.append(FillInTheBlank('In Michigan, snow falls in the month of _____', 'October'))
        self.problems.append(TrueFalse('Nike and Adidas are brother companies', False))
        self.problems.append(TrueFalse('Adidas and Puma are brother companies', True))
        self.problems.append(TrueFalse('CS 112 is easy', False))

        random.shuffle(self.problems)
        
        self.problemNum = 0
        
    def ask_current_question(self):
        ''' Return the text for the currently active question '''
        return self.problems[self.problemNum].ask_question()
    
    def get_current_answer(self):
        ''' Return the answer to the currently active question '''
        return self.problems[self.problemNum].get_answer()
    
    def check_current_answer(self, answer):
        ''' 
        Return True if answer is the answer to the currently active question, 
        False otherwise 
        '''
        return self.problems[self.problemNum].check_answer(answer)
    
    def has_next(self):
        ''' Return True if there are more questions; False otherwise '''
        return self.problemNum < len(self.problems) - 1
    
    def next(self):
        ''' Move on to the next question '''
        if self.problemNum == len(self.problems) - 1:
            raise Exception("There are no more problems")
        self.problemNum += 1
    
    
        