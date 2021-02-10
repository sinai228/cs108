'''This program uses exceptions and testing

Created Fall 2018

Lab 10

Sinai Park (sp46)
'''
# example
# try:
#     import happiness
# except ImportError as ie:
#     print('Dealt with ImportError: ', ie)


 #expression 1
try:
    'hi' + 4
except TypeError as ie:
    print('Dealt with TypeError: ', ie)
    
#expression 2
try:
    10/0
except ZeroDivisionError as ie:
    print('Dealt with ZeroDivisionError: ', ie)
    
#expression 3
try:
    'person'.find_first('e')
except AttributeError as ie:
    print('Dealt with AttributeError: ', ie)
    
#expression 4
try:
    [0, 1, 2]['summer']
except TypeError as ie:
    print('Dealt with TypeError: ', ie)
    
#expression 5
try:
    ['hi', 'there', 'student'][5]
except IndexError as ie:
    print('Dealt with IndexError:', ie)

#expression 6
try:
    print(name)
except NameError as ne:
    print('Dealt with NameError: ', ne)

#expression 7
try:
    9 <= (3, 4)
except TypeError as te:
    print('Dealt with TypeError: ', te)

#expression 8
try:
    f = open('missingFile.txt')
except FileNotFoundError as fe:
    print('Dealt with FileNotFoundError: ', fe)






