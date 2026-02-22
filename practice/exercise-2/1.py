''' Write a program to swap the contents of two variables using only bitwise operations. '''
a = int(input("Enter the first integer to swap : "))
b = int(input("Enter the second integer to swap : "))
print(f"Before swapping: a = {a}, b = {b}")
a = a ^ b
b = a ^ b
a = a ^ b
print(f"After swapping: a = {a}, b = {b}")