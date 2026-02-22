''' Write a program that takes as input two integers and prints appropriate messages if at least
one or both are positive, negative, or zero. '''
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
if num1 > 0 and num2 > 0:
    print("Both integers are positive.")
elif num1 < 0 and num2 < 0:
    print("Both integers are negative.")
elif num1 == 0 and num2 == 0:
    print("Both integers are zero.")
elif num1 > 0 or num2 > 0:
    print("At least one of the integers is positive.")
elif num1 < 0 or num2 < 0:
    print("At least one of the integers is negative.")
elif num1 == 0 or num2 == 0:
    print("At least one of the integers is zero.")
else:
    print("please enter valid integers.")