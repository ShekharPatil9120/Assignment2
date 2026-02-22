# ---------------------------------------------------
# Question 4: Age Calculator
# Ask user for birth year and calculate:
# 1. Current age
# 2. Age in months
# 3. Age in days (approx)
# 4. Age in hours
# 5. Age in minutes
# 6. Years remaining to reach 100
# ---------------------------------------------------

try:
    # Current year (you can update if needed)
    current_year = 2026

    # Taking input
    birth_year = int(input("Enter your birth year: "))

    # Validate input
    if birth_year > current_year or birth_year < 1900:
        print("Please enter a valid birth year.")
    else:
        # Age calculation
        age = current_year - birth_year

        # Conversions
        months = age * 12
        days = age * 365
        hours = days * 24
        minutes = hours * 60
        years_to_100 = 100 - age

        print("\n--- Age Details ---")
        print("Current Age:", age, "years")
        print("Age in Months:", months)
        print("Age in Days (approx):", days)
        print("Age in Hours:", hours)
        print("Age in Minutes:", minutes)

        if years_to_100 > 0:
            print("Years left to reach 100:", years_to_100)
        else:
            print("You have already reached or crossed 100 years!")

except:
    print("Invalid input! Please enter a valid year.")