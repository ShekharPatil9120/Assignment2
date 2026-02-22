# ---------------------------------------------------
# Question 10: ATM Simulator
# Bonus Added: Transaction History
# ---------------------------------------------------
balance = 10000
transactions = []   # list to store history

while True:
    print("\nATM MENU")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == '1':
            print("Current Balance:", balance)

        elif choice == '2':
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            transactions.append(f"Deposited: ₹{amount}")
            print("Deposit successful")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: "))
            if balance - amount >= 500:
                balance -= amount
                transactions.append(f"Withdrawn: ₹{amount}")
                print("Withdrawal successful")
            else:
                print("Minimum balance ₹500 must remain")

        elif choice == '4':
            print("\n--- Transaction History ---")
            if transactions:
                for t in transactions:
                    print(t)
            else:
                print("No transactions yet")

        elif choice == '5':
            break

        else:
            print("Invalid choice")

    except:
        print("Invalid input")