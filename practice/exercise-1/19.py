''' Write a program that takes a 2-letter word as input and prints it in small letters.
Note: Each letter of the input word can be in capital or small letters. '''
word = input("Enter a 2-letter word: ")
if len(word) == 2 and word.isalpha():
    small_word = word.lower()
    print(f"The word in small letters is: {small_word}")
else:
    print("Please enter a valid 2-letter word consisting of only letters.")
    
    
''' without using built-in functions '''
word = input("Enter a 2-letter word: ")
if len(word) == 2 and word.isalpha():
    small_word = ""
    for char in word:
        if 'A' <= char <= 'Z':
            small_char = chr(ord(char) + (ord('a') - ord('A')))
        else:
            small_char = char
        small_word += small_char
    print(f"The word in small letters is: {small_word}")
else:
    print("Please enter a valid 2-letter word consisting of only letters.")
    
    
    
''' without for loop'''
word = input("Enter a 2-letter word: ")
if len(word) == 2 and word.isalpha():
    char1 = word[0]
    char2 = word[1]
    if 'A' <= char1 <= 'Z':
        small_char1 = chr(ord(char1) + (ord('a') - ord('A')))
    else:
        small_char1 = char1
    if 'A' <= char2 <= 'Z':
        small_char2 = chr(ord(char2) + (ord('a') - ord('A')))
    else:
        small_char2 = char2
    small_word = small_char1 + small_char2
    print(f"The word in small letters is: {small_word}")