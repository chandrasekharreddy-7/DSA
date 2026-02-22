''' Write a program to swap two integers without using a third variable. '''
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
print(f"Before swapping: a = {a}, b = {b}")
a = a + b
b = a - b
a = a - b
print(f"After swapping: a = {a}, b = {b}")