''' Write a program that takes three integers as input and prints the minimum (of the three
values). '''
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
c = int(input("Enter the third integer: "))
if a <= b and a <= c:
    min_value = a
elif b <= a and b <= c:
    min_value = b
else:
    min_value = c
print(f"The minimum value among {a}, {b}, and {c} is: {min_value}")