''' Write a program that takes a number between 0 and 31 and prints its binary representation.
Note: Do not use the bin function '''
num = int(input("Enter a number between 0 and 31: "))
if 0 <= num <= 31:
    binary_representation = ""
    while num > 0:
        remainder = num % 2
        binary_representation = str(remainder) + binary_representation
        num //= 2
    if binary_representation == "":
        binary_representation = "0"
    print(f"The binary representation is: {binary_representation}")