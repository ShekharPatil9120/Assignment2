# Program: Simple calculator
# Description: Performs basic arithmetic operations

a = float(input())            # first number
b = float(input())            # second number
op = input()                  # operator

if op == '+':                 # addition
    print(a + b)
elif op == '-':               # subtraction
    print(a - b)
elif op == '*':               # multiplication
    print(a * b)
elif op == '/':               # division
    if b != 0:
        print(a / b)
    else:
        print("Invalid")
else:
    print("Invalid")