# ---------------------------------------------------
# Question 8: Leap Year Checker
# A year is a leap year if:
# - Divisible by 4 AND
# - Not divisible by 100 OR divisible by 400
# Display result along with reason
# ---------------------------------------------------

try:
    # Taking input from user
    year = int(input("Enter a year: "))

    # Checking leap year conditions
    if year % 400 == 0:
        print(f"{year} is a Leap Year")
        print("Reason: Divisible by 400")

    elif year % 100 == 0:
        print(f"{year} is NOT a Leap Year")
        print("Reason: Divisible by 100 but not by 400")

    elif year % 4 == 0:
        print(f"{year} is a Leap Year")
        print("Reason: Divisible by 4 and not by 100")

    else:
        print(f"{year} is NOT a Leap Year")
        print("Reason: Not divisible by 4")

except:
    print("Invalid input! Please enter a valid year.")