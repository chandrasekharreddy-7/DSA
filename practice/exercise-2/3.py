''' Write a program that takes an integer as input and checks, using bitwise operations, if it is
divisible by 4. '''
number = int(input("Enter an integer: "))
if (number & 3) == 0:
    print(f"{number} is divisible by 4.")
else:
    print(f"{number} is not divisible by 4.")
    