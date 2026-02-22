''' Write a program that takes a 4-character binary number and prints its decimal equivalent.
Note: Do not use hex, bin, or int functions. without enumerate '''
binary_num = input("Enter a 4-character binary number: ")
if len(binary_num) == 4 and all(c in "01" for c in binary_num):
    decimal_value = 0
    power = 3
    for char in binary_num:
        decimal_value += int(char) * (2 ** power)
        power -= 1
    print(f"The decimal equivalent of {binary_num} is: {decimal_value}")
else:
    print("Invalid input. Please enter a valid 4-character binary number.")