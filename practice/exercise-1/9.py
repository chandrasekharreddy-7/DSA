''' Write a program that takes the marks for 5 subjects as input and calculates the total and
average marks. '''
subject1 = float(input("Enter marks for subject 1: "))
subject2 = float(input("Enter marks for subject 2: "))
subject3 = float(input("Enter marks for subject 3: "))
subject4 = float(input("Enter marks for subject 4: "))
subject5 = float(input("Enter marks for subject 5: "))
total_marks = subject1 + subject2 + subject3 + subject4 + subject5
average_marks = total_marks / 5
print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")