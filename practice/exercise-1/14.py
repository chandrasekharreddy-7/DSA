''' Write a program that takes a valid letter grade (S/A/B/C/D/E) as input and prints its
respective grade point (10/9/8/7/6/4).
Note: If an invalid letter grade is entered, the program should display an appropriate
message. '''
grade = input("Enter a letter grade (S/A/B/C/D/E): ").upper()
if grade == 'S' or grade == 'A' or grade == 'B' or grade == 'C' or grade == 'D' or grade == 'E':
    if grade == 'S':
        grade_point = 10
    elif grade == 'A':
        grade_point = 9
    elif grade == 'B':
        grade_point = 8
    elif grade == 'C':
        grade_point = 7
    elif grade == 'D':
        grade_point = 6
    else:
        grade_point = 4
    print(f"The grade point for letter grade {grade} is: {grade_point}")
else:
    print("Invalid letter grade entered. Please enter a valid letter grade (S/A/B/C/D/E).")