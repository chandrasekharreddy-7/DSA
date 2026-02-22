''' Insurance Premium Calculation
A (hypothetical) insurance company wishes to automate its premium calculation and policy
restrictions. The rules are as follows:
(a) If a person's health is excellent, the person is between 25 and 35 years of age, lives
in a city, and is a male, then the premium is Rs. 4000 per month and the policy
amount cannot exceed Rs. 2 lakhs.
(b) If all the above conditions are satisfied except that the person is female, then the
premium is Rs. 3000 per month and the policy amount cannot exceed Rs. 1.5
lakhs.
(c) If a person's health is poor, the person is between 25 and 35 years of age, lives in
a village, and is a male, then the premium is Rs. 6000 per month and the policy
amount cannot exceed Rs. 1 lakh.
(d) In all other eligible cases, the premium is Rs. 5000 per month and the policy amount
cannot exceed Rs. 1.25 lakhs.
(e) A person below 25 years of age or above 65 years of age will not be insured.
(f) If the policy value requested is less than the maximum allowed, the monthly premium
amount is proportional to the policy value.
Write a program that takes necessary inputs from the user and determines whether the
person can be insured or not, and if eligible, calculates the premium amount to be paid. '''
health = input("Enter health status (excellent/poor): ").strip().lower()
age = int(input("Enter age: "))
residence = input("Enter residence (city/village): ").strip().lower()
gender = input("Enter gender (male/female): ").strip().lower()
policy_amount = float(input("Enter the desired policy amount: "))
if age < 25 or age > 65:
    print("The person cannot be insured due to age restrictions.") 
else:
    if health == "excellent" and residence == "city" and gender == "male":              
        max_policy_amount = 200000
        premium_rate = 4000
    elif health == "excellent" and residence == "city" and gender == "female":
        max_policy_amount = 150000
        premium_rate = 3000
    elif health == "poor" and residence == "village" and gender == "male":
        max_policy_amount = 100000
        premium_rate = 6000 
    else:
        max_policy_amount = 125000
        premium_rate = 5000
    if policy_amount > max_policy_amount:
        print(f"The requested policy amount exceeds the maximum allowed of Rs. {max_policy_amount}.")  
    else:
        premium = (policy_amount / max_policy_amount) * premium_rate
        print(f"The person can be insured. The monthly premium amount is: Rs. {premium:.2f}.")  
        