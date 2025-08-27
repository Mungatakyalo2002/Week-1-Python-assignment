# My Simple Calculator Program

# Input two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Choose an operation
operation = input("Enter operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 != 0:  
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Math Error: Cannot divide by zero!")