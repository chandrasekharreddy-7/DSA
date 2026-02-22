''' Write a program that takes a three-digit integer as input and prints the sum of its digits. '''
num = int(input("Enter a three-digit integer: "))
if 100 <= num <= 999:
    digit1 = num // 100
    digit2 = (num % 100) // 10
    digit3 = num % 10
    sum_of_digits = digit1 + digit2 + digit3
    print(f"The sum of the digits of {num} is: {sum_of_digits}")
else:
    print("Please enter a valid three-digit integer.")