# Program: Fibonacci series
# Description: Prints first n Fibonacci numbers

n = int(input())                   # take number of terms

a = 0                              # first number
b = 1                              # second number

for i in range(n):                 # loop n times
    print(a)                       # print current term
    c = a + b                      # next term
    a = b                          # update values
    b = c