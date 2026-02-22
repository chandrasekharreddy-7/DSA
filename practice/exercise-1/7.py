''' Write a program that takes three integers as input and prints their maximum value. '''
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
if a >= b and a >= c:
    max_value = a
elif b >= a and b >= c:
    max_value = b
else:
    max_value = c
print(f"The maximum value among {a}, {b}, and {c} is: {max_value}")