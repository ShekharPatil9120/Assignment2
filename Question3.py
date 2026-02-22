# Program: Even or Odd
# Description: Checks whether a number is even or odd

try:
    num = int(input())              # take number input

    if num % 2 == 0:                # check divisibility by 2
        print("Even")               # number is even
    else:
        print("Odd")                # number is odd

except:
    print("Invalid Input")          # handle invalid input