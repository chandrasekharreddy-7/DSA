''' Write a program that takes the radius of a circle as input and computes its area.
Note: If the radius is non-negative, display an appropriate message. '''
radius = float(input("Enter the radius of the circle: "))
if radius < 0:
    print("Radius cannot be negative. Please enter a non-negative value.")
else:
    area = 3.14 * radius ** 2
    print(f"The area of the circle with radius {radius} is: {area}")