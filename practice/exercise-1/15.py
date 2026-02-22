''' Write a program to select one option from the list and display output accordingly.
Example:
Please enter your choice:
1. Check Balance
2. View Offers
3. Special Recharge
Enter 0 to exit
(Display some arbitrary message for each option, e.g., “Your balance is Rs. 500”.) '''
print("Please enter your choice:")
print("1. Check Balance")
print("2. View Offers")
print("3. Special Recharge")
choice = int(input("Enter 0 to exit: "))
if choice == 1:
    print("Your balance is Rs. 500.")
elif choice == 2:
    print("Today's offers: 20% off on all recharges.")
elif choice == 3:
    print("Special Recharge: Get 1GB data for Rs. 50.")
elif choice == 0:
    print("Exiting the program. Thank you!")
else:
    print("Invalid choice. Please enter a valid option (0-3).")