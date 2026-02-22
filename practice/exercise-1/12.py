''' Write a program that takes a floating-point value as input and prints its absolute value. '''
value = float(input("Enter a floating-point value: "))
if value < 0:
    absolute_value = -value
else:
    absolute_value = value
print(f"The absolute value of {value} is: {absolute_value}")