''' Write a program to check whether a number has 0 as its last digit. '''
number = int(input("Enter an integer: "))
if number % 10 == 0:
    print(f"{number} has 0 as its last digit.")
else:
    print(f"{number} does not have 0 as its last digit.")