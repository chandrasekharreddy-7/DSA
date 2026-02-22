''' Write a program that takes an integer as input, and displays whether this integer is negative,
positive, or zero. '''
num = int(input("Enter an integer: "))
if num > 0:
    print(f"The integer {num} is positive.")
elif num < 0:
    print(f"The integer {num} is negative.")
else:
    print("The integer is zero.")