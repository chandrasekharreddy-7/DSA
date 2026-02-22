''' Write a program that takes a date in the format DDMMYYYY and prints the day of the week it
falls on. Given: 01-01-1990 was a Monday. '''
date_input = input("Enter a date in the format DDMMYYYY: ")
day = int(date_input[0:2])
month = int(date_input[2:4])
year = int(date_input[4:8])
# Zeller's Congruence algorithm to calculate the day of the week
if month < 3:
    month += 12
    year -= 1
K = year % 100
J = year // 100
f = day + (13 * (month + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)
day_of_week = f % 7
days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print(f"The day of the week for {date_input} is: {days[day_of_week]}")
