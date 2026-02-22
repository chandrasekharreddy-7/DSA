''' Write a program that takes the length and breadth of a rectangle as input and prints its area
and perimeter.
Note: If the inputs are invalid, display an appropriate message. '''
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
if length < 0 or breadth < 0:
    print("Length and breadth cannot be negative. Please enter non-negative values.")
else:
    area = length * breadth
    perimeter = 2 * (length + breadth)
    print(f"The area of the rectangle is: {area}")
    print(f"The perimeter of the rectangle is: {perimeter}")