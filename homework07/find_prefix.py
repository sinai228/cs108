'''
Making a figure of my own design (olympics)

Created on Oct 22, 2018

Homework 07

@author: Sinai Park (sp46)
'''

str1 = str(input('Please enter the first string:'))
str2= str(input('Please enter the second string:'))

def find_prefix(str1, str2):
    '''this function finds and prints the longest prefix of two strings'''
    prefix = ''
    for x in range(0, len(str1)):
        if str1[0] != str2[0]:
            return 'There is no prefix: %s' %prefix
        elif str1[x] == str2[x]:
            prefix += str1[x]
        else:
            return 'The longest prefix is: %s' %prefix
    return 'The longest prefix is: %s' %prefix
print(find_prefix(str1, str2))

def test_find_prefix():
    '''this function is used to test the function find_prefix'''
    print('\n')
    print(find_prefix('reenter', 'redeposit'))
    print(find_prefix('coding', 'programming'))
    print(find_prefix('prepare', 'perfect'))
    print(find_prefix('previous', 'prerequisite'))
    print(find_prefix('awesome', 'awesomeness'))
    print(find_prefix('hi computer', 'hi computer'))
    print(find_prefix('hi computer', 'hicomputer'))
    return ''
    
print(test_find_prefix())