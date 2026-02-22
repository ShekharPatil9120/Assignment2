# ---------------------------------------------------
# Question 15: Prime Number Checker
# ---------------------------------------------------

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

try:
    number = int(input("Enter a number: "))
    if is_prime(number):
        print(number, "is PRIME")
    else:
        print(number, "is NOT PRIME")

    start = int(input("Enter start range: "))
    end = int(input("Enter end range: "))

    print("Prime numbers in range:")
    for n in range(start, end + 1):
        if is_prime(n):
            print(n, end=" ")

except:
    print("Invalid input")