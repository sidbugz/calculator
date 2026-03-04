print("=== Simple Calculator ===")

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
except ValueError:
    print("Error: Please enter valid numbers only.")
    exit()

operation = input("Enter operation (+, -, *, /, %, **): ")

result = None

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        print("Error: Can't divide by zero!")
    else:
        result = num1 / num2
elif operation == "%":
    result = num1 % num2
elif operation == "**":
    result = num1 ** num2
else:
    print("I don't recognize that operation.")

if result is not None:
    print("Result:", result)