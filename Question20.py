# Program: Number pyramid
# Description: Prints pyramid pattern

n = int(input())                       # number of rows

for i in range(1, n + 1):              # loop through rows
    for j in range(n - i):             # print spaces
        print(" ", end="")
    for k in range(1, i + 1):          # print numbers
        print(k, end="")
    print()                            # next line