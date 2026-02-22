# Program: Armstrong number
# Description: Checks whether a number is Armstrong

num = int(input())                     # take input
temp = num                             # store original number
digits = len(str(num))                 # count digits
total = 0                              # initialize sum

while temp > 0:                        # extract digits
    digit = temp % 10                  # get last digit
    total += digit ** digits           # power and add
    temp = temp // 10                  # remove last digit

if total == num:                       # compare result
    print("Armstrong")
else:
    print("Not Armstrong")