# ---------------------------------------------------
# Question 7: Temperature Converter (Menu based)
# ---------------------------------------------------

while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    choice = input("Enter choice: ")

    try:
        if choice == '1':
            c = float(input("Enter Celsius: "))
            print("Fahrenheit:", (c * 9/5) + 32)

        elif choice == '2':
            f = float(input("Enter Fahrenheit: "))
            print("Celsius:", (f - 32) * 5/9)

        elif choice == '3':
            c = float(input("Enter Celsius: "))
            print("Kelvin:", c + 273.15)

        elif choice == '4':
            k = float(input("Enter Kelvin: "))
            print("Celsius:", k - 273.15)

        elif choice == '5':
            f = float(input("Enter Fahrenheit: "))
            print("Kelvin:", (f - 32) * 5/9 + 273.15)

        elif choice == '6':
            k = float(input("Enter Kelvin: "))
            print("Fahrenheit:", (k - 273.15) * 9/5 + 32)

        elif choice == '7':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

    except:
        print("Invalid input")