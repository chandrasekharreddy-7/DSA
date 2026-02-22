''' Write a program that takes as input:
• center of a circle (cx, cy),
• radius r,
• a point P(px, py),
and determines whether the point lies inside the circle, on the circle, or outside the circle. '''
cx, cy = float(input("Enter the x-coordinate of the center of the circle: ")), float(input("Enter the y-coordinate of the center of the circle: "))
r = float(input("Enter the radius of the circle: "))
px, py = float(input("Enter the x-coordinate of the point P: ")), float(input("Enter the y-coordinate of the point P: "))
distance_squared = (px - cx) ** 2 + (py - cy) ** 2
if distance_squared < r ** 2:
    print("The point P lies inside the circle.")
elif distance_squared == r ** 2:
    print("The point P lies on the circle.")
else:
    print("The point P lies outside the circle.")
