''' Write a program that takes a 4-letter word as input and toggles the case of all its letters
using bitwise operations. Example: Input: HeLLo
Output: hEllO '''
word = input("Enter a 4-letter word: ")
if len(word) == 4:
    toggled_word = ""
    for char in word:
        if 'a' <= char <= 'z':
            toggled_char = chr(ord(char) ^ 32)
        elif 'A' <= char <= 'Z':
            toggled_char = chr(ord(char) ^ 32)
        else:
            toggled_char = char
        toggled_word += toggled_char
    print(f"Toggled case: {toggled_word}")