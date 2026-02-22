''' Write a program that takes as input two integers and checks if their LCM is equal to at least
one of the given integers. '''
''' without build in function and without using GCD and loops and max'''
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
if num1 == 0 or num2 == 0:
    print("LCM is zero.")
else:
    if num1 > num2:
        greater = num1
    else:
        greater = num2
    while greater % num1 != 0 or greater % num2 != 0:
        greater = greater + 1
    lcm = greater
    if lcm == num1 or lcm == num2:
        print("LCM is equal to at least one of the given integers.")
    else:
        print("LCM is not equal to any of the given integers.")