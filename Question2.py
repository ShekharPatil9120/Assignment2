# Program: Factorial of a number
# Description: Finds the factorial using a loop

try:
    num = int(input())          # take number input

    if num < 0:                 # check for negative number
        print("Invalid Input")  # factorial not defined for negative
    else:
        fact = 1                # initialize factorial value
        for i in range(1, num + 1):  # loop from 1 to num
            fact = fact * i     # multiply each number
        print(fact)             # display result

except:
    print("Invalid Input")      # handle invalid input