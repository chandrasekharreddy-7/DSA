''' Write a program that takes a character as input and prints the alpha-numeric character (0 - 9,
A - Z, a - z are alpha-numeric characters) that is closest to this character.
Note: If the input character is equidistant from two alpha-numeric values, either one can
be printed. '''
char = input("Enter a character: ")
''' without using built-in functions '''
if '0' <= char <= '9' or 'A' <= char <= 'Z' or 'a' <= char <= 'z':
    closest_char = char
elif char < '0':
    closest_char = '0'
elif '9' < char < 'A':
    closest_char = '9' if (ord(char) - ord('9')) <= (ord('A') - ord(char)) else 'A'
elif 'Z' < char < 'a':
    closest_char = 'Z' if (ord(char) - ord('Z')) <= (ord('a') - ord(char)) else 'a'
elif char > 'z':
    closest_char = 'z'
else:
    closest_char = char
print(f"The closest alpha-numeric character to '{char}' is: '{closest_char}'")