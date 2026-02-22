# ---------------------------------------------------
# Question 5: Bill Splitter
# Inputs:
# Total bill amount
# Number of people
# Tax percentage
# Tip percentage
#
# Display:
# Subtotal, Tax amount, After tax,
# Tip amount, Total bill, Amount per person
# ---------------------------------------------------

try:
    # Taking inputs
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))
    tax_percent = float(input("Enter tax percentage: "))
    tip_percent = float(input("Enter tip percentage: "))

    # Basic validation
    if people <= 0:
        print("Number of people must be greater than 0")
    else:
        # Calculations
        subtotal = total_bill

        tax_amount = subtotal * (tax_percent / 100)
        after_tax = subtotal + tax_amount

        tip_amount = after_tax * (tip_percent / 100)
        total_amount = after_tax + tip_amount

        per_person = total_amount / people

        # Output
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax ({tax_percent}%): ₹{tax_amount:.2f}")
        print(f"After tax: ₹{after_tax:.2f}")
        print(f"Tip ({tip_percent}%): ₹{tip_amount:.2f}")
        print(f"Total: ₹{total_amount:.2f}")
        print(f"Per person: ₹{per_person:.2f}")

except:
    print("Invalid input! Please enter correct values.")