''' Write a program that takes a natural number as input and prints the remainder when it is
divided by 3. '''
number = int(input("Enter a natural number: "))
if number >= 0:
    remainder = number % 3
    print(f"The remainder when {number} is divided by 3 is: {remainder}")
else:
    print("Please enter a valid natural number (0 or positive integer).")