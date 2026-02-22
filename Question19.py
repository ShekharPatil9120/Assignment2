# Program: Decimal to binary
# Description: Converts decimal number to binary

num = int(input())                     # take input
binary = ""                            # store binary

if num == 0:                           # special case
    binary = "0"
else:
    while num > 0:                     # convert using division
        binary = str(num % 2) + binary
        num = num // 2

print(binary)                          # display binary