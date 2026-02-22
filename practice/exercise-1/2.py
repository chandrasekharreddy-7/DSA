''' Write a program that takes two integers a and b as input and prints their sum, difference,
product, quotient, and remainder. '''
a = int(input("Enter the first integer : "))
b = int(input("Enter the second integer : "))
sum = a + b
difference = a - b
product = a * b
if b != 0:
    quotient = a / b
    remainder = a % b
    print(f"The sum of {a} and {b} is: {sum}")
    print(f"The difference of {a} and {b} is: {difference}")
    print(f"The product of {a} and {b} is: {product}")
    print(f"The quotient of {a} and {b} is: {quotient}")
    print(f"The remainder of {a} and {b} is: {remainder}")
else:
    print(f"The sum of {a} and {b} is: {sum}")
    print(f"The difference of {a} and {b} is: {difference}")
    print(f"The product of {a} and {b} is: {product}")
    print("Cannot divide by zero. Quotient and remainder are undefined.")