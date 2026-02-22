# ---------------------------------------------------
# Question 2: Simple Calculator
# Ask user for two numbers and perform:
# Addition, Subtraction, Multiplication,
# Division, Modulus, Exponent
# ---------------------------------------------------

# Taking input from user
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(f"{num1} + {num2} = {num1 + num2}")

    # Subtraction
    print(f"{num1} - {num2} = {num1 - num2}")

    # Multiplication
    print(f"{num1} * {num2} = {num1 * num2}")

    # Division (check for zero)
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Division by zero is not allowed")

    # Modulus (check for zero)
    if num2 != 0:
        print(f"{num1} % {num2} = {num1 % num2}")
    else:
        print("Modulus by zero is not allowed")

    # Exponent
    print(f"{num1} ^ {num2} = {num1 ** num2}")

except:
    print("Invalid input! Please enter numeric values only.")