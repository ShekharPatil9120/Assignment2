# Program: Largest of three numbers
# Description: Finds the largest among three numbers

try:
    a = int(input())                # take first number
    b = int(input())                # take second number
    c = int(input())                # take third number

    if a >= b and a >= c:           # check if a is largest
        print(a)
    elif b >= a and b >= c:         # check if b is largest
        print(b)
    else:
        print(c)                    # otherwise c is largest

except:
    print("Invalid Input")          # handle invalid input