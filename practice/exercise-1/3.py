''' Write a simple calculator program. It should be able to add, subtract, multiply, and divide
any two numbers input by the user.
Note: The user will also specify the operation to perform. '''
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation to perform (add, subtract, multiply, divide): ")
if operation in ["add", "Add", "ADD", "+"]:
    result = num1 + num2
    print(f"The result of adding {num1} and {num2} is: {result}")
elif operation in ["subtract", "Subtract", "SUBTRACT", "-"]:
    result = num1 - num2
    print(f"The result of subtracting {num2} from {num1} is: {result}")
elif operation in ["multiply", "Multiply", "MULTIPLY", "*"]:
    result = num1 * num2
    print(f"The result of multiplying {num1} and {num2} is: {result}")
elif operation in ["divide", "Divide", "DIVIDE", "/"]:
    if num2 != 0:
        result = num1 / num2
        print(f"The result of dividing {num1} by {num2} is: {result}")
    else:
        print("Cannot divide by zero. Please enter a non-zero value for the second number.")
else:
    print("Invalid operation. Please enter one of the following: add, subtract, multiply, divide.")