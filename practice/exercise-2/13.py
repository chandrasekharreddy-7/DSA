''' Write a program that takes three points (x1, y1), (x2, y2), and (x3, y3) and checks if they lie
on a straight line. '''
x1, y1 = int(input("Enter x1: ")), int(input("Enter y1: "))
x2, y2 = int(input("Enter x2: ")), int(input("Enter y2: "))
x3, y3 = int(input("Enter x3: ")), int(input("Enter y3: "))
if (y2 - y1) * (x3 - x1) == (y3 - y1) * (x2 - x1):
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")