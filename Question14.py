# ---------------------------------------------------
# Question 14: Factorial Calculator
# ---------------------------------------------------

try:
    n = int(input("Enter a number: "))

    if n < 0:
        print("Factorial not defined for negative numbers")
    else:
        factorial = 1
        steps = ""
        for i in range(n, 0, -1):
            factorial *= i
            steps += str(i)
            if i != 1:
                steps += " x "

        print(f"{n}! = {steps} = {factorial}")

except:
    print("Invalid input")