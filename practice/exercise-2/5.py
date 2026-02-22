''' Write a program that takes as input n1 o1 n2 o2 n3, where n1, n2, n3 are natural numbers
and o1, o2 ∈ {+, -, *}. Use nested if--else--if statements to evaluate the expression. '''
n1 = int(input("Enter the first natural number (n1): "))
o1 = input("Enter the first operator (o1) (+, -, *): ")
n2 = int(input("Enter the second natural number (n2): "))
o2 = input("Enter the second operator (o2) (+, -, *): ")
n3 = int(input("Enter the third natural number (n3): "))
if o1 == '+':
    if o2 == '+':
        result = n1 + n2 + n3
        print(f"The result of the expression is: {result}")
    elif o2 == '-':
        result = n1 + n2 - n3
        print(f"The result of the expression is: {result}")
    elif o2 == '*':
        result = n1 + (n2 * n3)
        print(f"The result of the expression is: {result}")
    else:
        print("Invalid operator for o2. Please use +, -, or *.")
elif o1 == '-':
    if o2 == '+':
        result = n1 - n2 + n3
        print(f"The result of the expression is: {result}")
    elif o2 == '-':
        result = n1 - n2 - n3
        print(f"The result of the expression is: {result}")
    elif o2 == '*':
        result = n1 - (n2 * n3)
        print(f"The result of the expression is: {result}")
    else:
        print("Invalid operator for o2. Please use +, -, or *.")
elif o1 == '*':
    if o2 == '+':
        result = (n1 * n2) + n3
        print(f"The result of the expression is: {result}")
    elif o2 == '-':
        result = (n1 * n2) - n3
        print(f"The result of the expression is: {result}")
    elif o2 == '*':
        result = n1 * n2 * n3
        print(f"The result of the expression is: {result}")
    else:
        print("Invalid operator for o2. Please use +, -, or *.")
else:
    print("Invalid operator for o1. Please use +, -, or *.")