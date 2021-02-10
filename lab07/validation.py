'''validation
October 18, 2018
Lab 7
@author: Hyungseok Park (hp46) Sinai Park (sp46)
'''
 
 
'''
define function that receives string SSN
    if number ssn in not equal to 11 then false
    elif [3] and [6] not equal to '-' then false
    replace '-' with empty string
    else print valid
    return true or false
'''    


def isValidSSN (SSN):
    ''' Print if SSN is valid'''
    if  len(SSN) != 11:
        return 'Invalid SSN'
    elif SSN[3] != '-' and SSN[6] != '-':
        return 'Invalid SSN'
    elif not SSN.replace('-', '').isdigit():
            return 'Invalid SSN'
    return 'Valid SSN'
 
 
def isValidPassword(password):
    ''' Print if Password is valid'''
    accumulator = 0
    if  len(password) <= 8:
        return 'Invalid Password'
    elif password.isalpha():
        return 'Invalid Password'
    for x in password:
        if x.isdigit():
            accumulator += 1
    if accumulator < 2:
        return 'Invalid password'
    return 'Valid Password'
         
def isValidPrefix(prefix):
    '''returns true or false for the validity of the first characters'''
    if prefix [:2] == '37':
        return True
    elif prefix [0] == '4':
        return True
    elif prefix [0] == '5':
        return True
    elif prefix [0] == '6':
        return True
    else:
        return False
 
def sum_of_odds(cardnumber):
    '''return sum of odd numbers counting backwards'''
    odd_list = 0
    if len(cardnumber) == 13 or len(cardnumber) == 15:
        for x in cardnumber[::-2]:
            odd_list += int(x) 
        return odd_list
    elif len(cardnumber) == 14 or len(cardnumber) == 16:
        for x in cardnumber[-1::-2]:
            odd_list += int(x)
        return odd_list
     
def sum_of_double_evens(string):
    '''return sum of double even and if 2 number digit add first and second index'''
    double_list = []
    for x in string[-2::-2]:
        double_list.append(int(x)*2)
         
    final_list = 0
    for x in double_list:
        if x <= 9:
            final_list += x
        elif x >= 10:
            x = 1 + x % 10
            final_list += x
    return final_list
 
 
def isValidCC (CC):
    '''Print of prefix of credit card number is valid'''

    if CC.isdigit() is True and isValidPrefix(CC) is True and (13 <= len(CC) <= 16) is True and ((sum_of_odds(CC) + sum_of_double_evens(CC)) % 10 == 0) is True:
        return "Valid Creditcard"
    
    return 'Invalid Credit Card'      
     
     
def printMenu():
    '''Print the text menu.'''
    print('\nPlease select from the following list of options (type the appropriate character):')
    print('A. Print a nice message')
    print('S. Verify valid SSN')
    print('P. Verify password')
    print('C. Verify credit card')
    # Add menu options here for three new string tests.
    print('Q. Quit')
 
 
# Run the text-menu interface until the user wants to quit.
while True:
    printMenu()
    choice = input('Choice: ').upper()
     
    if choice == 'A':
        print('Have a great day!')
         
    if choice == 'S':
        print(isValidSSN(input('Please enter your SSN:')))
         
    if choice == 'P':
        print(isValidSSN(input('Please enter your password:')))
         
    if choice == 'C':
        print(isValidCC(input('Please enter your credit card number:')))
         
    # Add code here to handle tests for the three string types.
    # Each option should read a value from the user, pass it to the appropriate check routine and print the result.
         
    elif choice == 'Q':
        break
    
    else:
        print('I\'m sorry, {0} is not a valid option.'.format(choice))
     
print('\nGood-bye!')
 
print(printMenu())

