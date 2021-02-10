'''
Models a true or false problem

Created Fall 2014

Lab 13

@author: Sinai Park(sp46)
'''
from problem import *


'''Constructor'''
class TrueFalse(Problem):
    ''' Model a short-answer question '''
    
    def __init__(self, q, a):
        ''' Construct a short-answer question with question and answer texts '''
        Problem.__init__(self, q)
        self.answer = a
        if not isinstance(self.answer, bool):
            raise AssertionError('Answer should be a boolean value.')
              
    def ask_question(self):
        ''' Return the question text '''
        return super().get_text() + '\nIs this statement True or False?' 
    
    def check_answer(self, a):
        ''' Return True if a is the correct answer; False otherwise '''
        return str(self.answer) == a
    
    def get_answer(self):
        ''' Return the answer text '''
        return str(self.answer)
    
    
if __name__ == "__main__":
    q = TrueFalse('question', True)
    assert q.get_text() == 'question'
    assert q.get_answer() == 'True'
    assert q.ask_question() == 'question\nIs this statement True or False?'
    assert not (q.check_answer('ans'))
    assert q.check_answer('True')
    print('All TrueFalse tests passed!')