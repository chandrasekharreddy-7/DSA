''' Write a program that takes two integers a and b as input and displays whether a < b, a = b,
or a > b. '''
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
if a < b:
    print(f"{a} is less than {b}.")
elif a > b:
    print(f"{a} is greater than {b}.")
else:
    print(f"{a} is equal to {b}.")