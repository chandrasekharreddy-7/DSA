''' Write a program that takes an integer as input and displays if it is odd or even. '''
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")