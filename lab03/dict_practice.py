'''
Working with dictionaries
Created on Sep 20, 2018

Lab 3

@author: Sinai Park (sp46), Gaby Pineda (gjp3), Yeheun Lee (yl55)
'''
#create dictionary with keys and values
scoreDict = {'Joe': 10, 'Tom': 23, 'Barb': 13, 'Sue': 19, 'Sally': 12}

#print barb's score
print('Barb\'s score is :', scoreDict['Barb'])

#update sallys score
scoreDict['Sally'] = 12

#remove tom from dict
scoreDict.pop('Tom')

#print the updated dict
print(scoreDict)