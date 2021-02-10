'''
Textual Analysis of Green Eggs and Ham

Created on Oct. 10, 2018

Lab06

@author: Sinai Park (sp46), Chiz Nnodu(cin2)

'''
from PIL.WmfImagePlugin import word

#Exercise 6.2 (empty list, list of 1 element, list of 3 or 4 elements)
empty_list = []
one_list = ['computerlab']
multiple_list = ['zero', 'hundred', 'thousand']


green_eggs_and_ham = [ "i", "am", "sam", "sam", "i", "am", "that",
            "sam-i-am", "that", "sam-i-am", "i", "do", "not", "like", "that", "sam-i-am", "do",
            "you", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them",
            "sam-i-am", "i", "do", "not", "like", "green", "eggs", "and", "ham", "would", "you",
            "like", "them", "here", "or", "there", "i", "would", "not", "like", "them", "here",
            "or", "there", "i", "would", "not", "like", "them", "anywhere", "i", "do", "not",
            "like", "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am",
            "would", "you", "like", "them", "in", "a", "house", "would", "you", "like", "them",
            "with", "a", "mouse", "i", "do", "not", "like", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would",
            "you", "eat", "them", "in", "a", "box", "would", "you", "eat", "them", "with", "a",
            "fox", "not", "in", "a", "box", "not", "with", "a", "fox", "not", "in", "a", "house",
            "not", "with", "a", "mouse", "i", "would", "not", "eat", "them", "here", "or", "there",
            "i", "would", "not", "eat", "them", "anywhere", "i", "would", "not", "eat", "green",
            "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "would", "you",
            "could", "you", "in", "a", "car", "eat", "them", "eat", "them", "here", "they", "are",
            "i", "would", "not", "could", "not", "in", "a", "car", "you", "may", "like", "them",
            "you", "will", "see", "you", "may", "like", "them", "in", "a", "tree", "not", "in",
            "a", "tree", "i", "would", "not", "could", "not", "in", "a", "tree", "not", "in", "a",
            "car", "you", "let", "me", "be", "i", "do", "not", "like", "them", "in", "a", "box",
            "i", "do", "not", "like", "them", "with", "a", "fox", "i", "do", "not", "like", "them",
            "in", "a", "house", "i", "do", "not", "like", "them", "with", "a", "mouse", "i", "do",
            "not", "like", "them", "here", "or", "there", "i", "do", "not", "like", "them",
            "anywhere", "i", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not",
            "like", "them", "sam-i-am", "a", "train", "a", "train", "a", "train", "a", "train",
            "could", "you", "would", "you", "on", "a", "train", "not", "on", "a", "train", "not",
            "in", "a", "tree", "not", "in", "a", "car", "sam", "let", "me", "be", "i", "would",
            "not", "could", "not", "in", "a", "box", "i", "could", "not", "would", "not", "with",
            "a", "fox", "i", "will", "not", "eat", "them", "with", "a", "mouse", "i", "will",
            "not", "eat", "them", "in", "a", "house", "i", "will", "not", "eat", "them", "here",
            "or", "there", "i", "will", "not", "eat", "them", "anywhere", "i", "do", "not", "like",
            "them", "sam-i-am", "say", "in", "the", "dark", "here", "in", "the", "dark", "would",
            "you", "could", "you", "in", "the", "dark", "i", "would", "not", "could", "not", "in",
            "the", "dark", "would", "you", "could", "you", "in", "the", "rain", "i", "would",
            "not", "could", "not", "in", "the", "rain", "not", "in", "the", "dark", "not", "on",
            "a", "train", "not", "in", "a", "car", "not", "in", "a", "tree", "i", "do", "not",
            "like", "them", "sam", "you", "see", "not", "in", "a", "house", "not", "in", "a",
            "box", "not", "with", "a", "mouse", "not", "with", "a", "fox", "i", "will", "not",
            "eat", "them", "here", "or", "there", "i", "do", "not", "like", "them", "anywhere",
            "you", "do", "not", "like", "green", "eggs", "and", "ham", "i", "do", "not", "like",
            "them", "sam-i-am", "could", "you", "would", "you", "with", "a", "goat", "i", "would",
            "not", "could", "not", "with", "a", "goat", "would", "you", "could", "you", "on", "a",
            "boat", "i", "could", "not", "would", "not", "on", "a", "boat", "i", "will", "not",
            "will", "not", "with", "a", "goat", "i", "will", "not", "eat", "them", "in", "the",
            "rain", "i", "will", "not", "eat", "them", "on", "a", "train", "not", "in", "the",
            "dark", "not", "in", "a", "tree", "not", "in", "a", "car", "you", "let", "me", "be",
            "i", "do", "not", "like", "them", "in", "a", "box", "i", "do", "not", "like", "them",
            "with", "a", "fox", "i", "will", "not", "eat", "them", "in", "a", "house", "i", "do",
            "not", "like", "them", "with", "a", "mouse", "i", "do", "not", "like", "them", "here",
            "or", "there", "i", "do", "not", "like", "them", "anywhere", "i", "do", "not", "like",
            "green", "eggs", "and", "ham", "i", "do", "not", "like", "them", "sam-i-am", "you",
            "do", "not", "like", "them", "so", "you", "say", "try", "them", "try", "them", "and",
            "you", "may", "try", "them", "and", "you", "may", "i", "say", "sam", "if", "you",
            "will", "let", "me", "be", "i", "will", "try", "them", "you", "will", "see", "say",
            "i", "like", "green", "eggs", "and", "ham", "i", "do", "i", "like", "them", "sam-i-am",
            "and", "i", "would", "eat", "them", "in", "a", "boat", "and", "i", "would", "eat",
            "them", "with", "a", "goat", "and", "i", "will", "eat", "them", "in", "the", "rain",
            "and", "in", "the", "dark", "and", "on", "a", "train", "and", "in", "a", "car", "and",
            "in", "a", "tree", "they", "are", "so", "good", "so", "good", "you", "see", "so", "i",
            "will", "eat", "them", "in", "a", "box", "and", "i", "will", "eat", "them", "with",
            "a", "fox", "and", "i", "will", "eat", "them", "in", "a", "house", "and", "i", "will",
            "eat", "them", "with", "a", "mouse", "and", "i", "will", "eat", "them", "here", "and",
            "there", "say", "i", "will", "eat", "them", "anywhere", "i", "do", "so", "like",
            "green", "eggs", "and", "ham", "thank", "you", "thank", "you", "sam-i-am"]

#Exercise 6.5
stop_words = [ "a", "able", "about", "across", "after", "all",
            "almost", "also", "am", "among", "an", "and", "any", "are", "as", "at", "be",
            "because", "been", "but", "by", "can", "cannot", "could", "dear", "did", "do", "does",
            "either", "else", "ever", "every", "for", "from", "get", "got", "had", "has", "have",
            "he", "her", "hers", "him", "his", "how", "however", "i", "if", "in", "into", "is",
            "it", "its", "just", "least", "let", "like", "likely", "may", "me", "might", "most",
            "must", "my", "neither", "no", "nor", "not", "of", "off", "often", "on", "only", "or",
            "other", "our", "own", "rather", "said", "say", "says", "she", "should", "since", "so",
            "some", "than", "that", "the", "their", "them", "then", "there", "these", "they",
            "this", "tis", "to", "too", "twas", "us", "wants", "was", "we", "were", "what", "when",
            "where", "which", "while", "who", "whom", "why", "will", "with", "would", "yet", "you",
            "your" ]

#Exercise 6.4 (algorithm)
'''
define function longest_and_shortest
for word in str_list 
compute longest and shortest variable as index 0
loop through all the words in str_list to determine whether word is longer or shorter
    if length is longer or shorter
        assign new word to longest/shortest variable
    return -1
    
print longest word
print shortest word

'''

def longest_and_shortest(str_list):
    'this function receives a list of words and prints the length of the shortest and the longest word in the list'
    shortest = str_list[0]
    longest = str_list[0]
    for word in str_list[1:]:
        if len(word) < len(str_list[0]): 
            shortest = word
        elif len(word) > len(str_list[0]):
            longest = word
        elif len(str_list) == 0:
            print('The given list was empty.')
        
    print('The length of the shortest word is: '+ shortest +'\n'+ 'The length of the longest word is: ' + longest)
        
        
        
        
#Exercise 6.3
def search(str_list, target):
    'this function searches through a list of words looking for a given target word'
    position = 0
    for element in str_list:
        if target == element:
            return position
        position += 1
    return -1


def test_search():
    'this function tests that my search function is correct (bad input values, etc)'
    print(search(empty_list, 'hi'))
    print(search(multiple_list, 'box'))
    print(search(multiple_list, 'zero'))
    print(search(green_eggs_and_ham, 'will'))
    
    

#EXTRACREDIT EXERCISE 6.6
def count_unique_words(str_list):
    count = 0
    unique_words = []
    for word in str_list:
        if word not in unique_words:
            unique_words.append(word)
            count += 1
    return count

def test_count_unique_words():
    print(count_unique_words(green_eggs_and_ham))

print('\n')
test_count_unique_words()



def green_eggs_and_ham_analysis():
    'this function analyzes the green eggs and ham to print out an index for the following words'
    print(search(green_eggs_and_ham, 'i' ))
    print(search(green_eggs_and_ham, 'boat'))
    print(search(green_eggs_and_ham, 'fox'))
    print(search(green_eggs_and_ham, 'thank'))
    print(search(green_eggs_and_ham, 'book'))
    
    longest_and_shortest(green_eggs_and_ham)
    print(count_unique_words(green_eggs_and_ham))
    
green_eggs_and_ham_analysis()  
    
    
#Exercise 6.1
print('\n')
print(len(green_eggs_and_ham))

search(green_eggs_and_ham, 'tree')

#calling the test function and the analysis function
test_search()  

print('\n')




#Exercise 6.5
'''
define the function(list 1, list 2)
for first word in list 1 loop through list 2 
determine whether word in list 1 appears in list 2
if word is not found in list 2 , assign word to a new list
print list of words that do not appear
'''

#create test lists for the function
listone = ['hi', 'hello', 'bye']
listtwo = ['hi', 'bi', 'bellow']

def count_words_not_present (list1, list2):
    counter = 0
    for word in list1 :
        if search(list2, word) == -1:
            counter += 1
    print(counter)
    
#test function
def test_count_words_not_present():
    count_words_not_present(listone, listtwo)
    count_words_not_present(green_eggs_and_ham, stop_words)
test_count_words_not_present()


