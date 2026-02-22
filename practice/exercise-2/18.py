''' A library charges a fine for late returns:
• First 5 days: 50 paise
• 6 - 10 days: 1 rupee
• Above 10 days: 5 rupees
If returned after 30 days, membership is canceled. Write a program to display the fine or
the appropriate message. '''
days_late = int(input("Enter the number of days the book is late: "))
if days_late <= 5:
    fine = days_late * 0.50
    print(f"The fine is: {fine} rupees")
elif 6 <= days_late <= 10:
    fine = (5 * 0.50) + ((days_late - 5) * 1)
    print(f"The fine is: {fine} rupees")
elif 11 <= days_late <= 30:
    fine = (5 * 0.50) + (5 * 1) + ((days_late - 10) * 5)
    print(f"The fine is: {fine} rupees")
else:
    print("Membership is cancelled.")