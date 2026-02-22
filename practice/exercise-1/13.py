''' Write a program that takes an integer as input and checks if it is divisible by 17. '''
number = int(input("Enter an integer: "))
if number % 17 == 0:
    print(f"{number} is divisible by 17.")
else:
    print(f"{number} is not divisible by 17.")