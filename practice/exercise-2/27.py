''' Write a program that takes a 4-character hexadecimal number and prints its decimal equiv-
alent. Note: Do not use hex, bin, or int functions. '''
hex_num = input("Enter a 4-character hexadecimal number: ")
if len(hex_num) == 4 and all(c in "0123456789abcdefABCDEF" for c in hex_num):
    decimal_value = 0
    for i, char in enumerate(reversed(hex_num)):
        if char.isdigit():
            decimal_value += int(char) * (16 ** i)
        else:
            decimal_value += (ord(char.upper()) - ord('A') + 10) * (16 ** i)
    print(f"The decimal equivalent of {hex_num} is: {decimal_value}")