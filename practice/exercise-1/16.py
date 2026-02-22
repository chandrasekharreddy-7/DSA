''' Write a program that takes as input the coefficients of the quadratic equation

ax2 + bx + c = 0
and prints whether the roots are real or complex. '''
a = float(input("Enter the coefficient of x^2 : "))
b = float(input("Enter the coefficient of x : "))
c = float(input("Enter the constant term : "))
d = b**2 - 4*a*c
if d > 0:
    print("The roots are real and distinct.")
elif d == 0:
    print("The roots are real and equal.")
else:
    print("The roots are complex.")