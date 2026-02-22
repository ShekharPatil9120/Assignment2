# ---------------------------------------------------
# Question 9: Movie Ticket Pricing System
# Age-based pricing and weekend discount
# ---------------------------------------------------

try:
    # Taking inputs
    age = int(input("Enter age: "))
    day = input("Enter day of week: ").strip().lower()
    tickets = int(input("Enter number of tickets: "))

    # Check valid ticket count
    if tickets <= 0:
        print("Number of tickets must be greater than 0")

    else:
        # Age-based pricing
        if age < 3:
            price_per_ticket = 0
            category = "Free"
        elif 3 <= age <= 12:
            price_per_ticket = 150
            category = "Child"
        elif 13 <= age <= 59:
            price_per_ticket = 300
            category = "Adult"
        else:
            price_per_ticket = 200
            category = "Senior"

        # Base amount
        base_amount = price_per_ticket * tickets

        # Day-based discount (Friday to Sunday)
        if day in ["friday", "saturday", "sunday"]:
            discount = base_amount * 0.20
        else:
            discount = 0

        final_amount = base_amount - discount

        # Display bill details
        print("\n--- Ticket Details ---")
        print("Category:", category)
        print("Price per ticket: ₹", price_per_ticket)
        print("Number of tickets:", tickets)
        print("Base price: ₹", base_amount)
        print("Discount: ₹", discount)
        print("Final amount to pay: ₹", final_amount)

except:
    print("Invalid input! Please enter correct values.")