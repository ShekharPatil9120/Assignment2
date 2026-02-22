# Program: Prime number check
# Description: Checks whether a number is prime

num = int(input())                 # take number input
is_prime = True                    # assume number is prime

if num <= 1:                       # numbers <= 1 are not prime
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):  # check up to square root
        if num % i == 0:           # if divisible
            is_prime = False       # not prime
            break

if is_prime:                       # print result
    print("Prime")
else:
    print("Not Prime")