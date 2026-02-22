''' Write a program that takes a 2-letter word as input and prints it in capital letters.
Note: Each letter of the input word can be in capital or small letters. '''
word = input("Enter a 2-letter word: ")
if len(word) == 2 and word.isalpha():
    capitalized_word = word.upper()
    print(f"The word in capital letters is: {capitalized_word}")
else:
    print("Please enter a valid 2-letter word consisting of only letters.")


''' without using built-in functions '''
word = input("Enter a 2-letter word: ")
if len(word) == 2 and word.isalpha():
    capitalized_word = ""
    for char in word:
        if 'a' <= char <= 'z':
            capitalized_char = chr(ord(char) - (ord('a') - ord('A')))
        else:
            capitalized_char = char
        capitalized_word += capitalized_char
    print(f"The word in capital letters is: {capitalized_word}")
else:
    print("Please enter a valid 2-letter word consisting of only letters.")
    
    
    
''' without for loop'''
word = input("Enter a 2-letter word: ")
if len(word) == 2 and word.isalpha():
    char1 = word[0]
    char2 = word[1]
    if 'a' <= char1 <= 'z':
        capitalized_char1 = chr(ord(char1) - (ord('a') - ord('A')))
    else:
        capitalized_char1 = char1
    if 'a' <= char2 <= 'z':
        capitalized_char2 = chr(ord(char2) - (ord('a') - ord('A')))
    else:
        capitalized_char2 = char2
    capitalized_word = capitalized_char1 + capitalized_char2
    print(f"The word in capital letters is: {capitalized_word}")