# Program: Sum of digits
# Description: Finds sum of digits of a number

try:
    num = int(input())              # take number input
    total = 0                       # initialize sum

    num = abs(num)                  # handle negative numbers

    while num > 0:                  # loop until number becomes 0
        digit = num % 10            # get last digit
        total += digit              # add digit to sum
        num = num // 10             # remove last digit

    print(total)                    # display result

except:
    print("Invalid Input")          # handle invalid input