''' Write a program that takes a point P(px, py) and determines the quadrant it lies in. Explicitly
handle the cases when the point lies on the axes or at the origin. '''
px, py = float(input("Enter the x-coordinate of the point P: ")), float(input("Enter the y-coordinate of the point P: "))
if px > 0 and py > 0:
    print("The point P lies in the first quadrant.")
elif px < 0 and py > 0:
    print("The point P lies in the second quadrant.")
elif px < 0 and py < 0:
    print("The point P lies in the third quadrant.")
elif px > 0 and py < 0:
    print("The point P lies in the fourth quadrant.")
elif px == 0 and py == 0:
    print("The point P lies at the origin.")
elif px == 0:
    print("The point P lies on the y-axis.")
else:
    print("The point P lies on the x-axis.")