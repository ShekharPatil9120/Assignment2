# ---------------------------------------------------
# Question 11: Number Pattern Printer
# User chooses pattern and height
# ---------------------------------------------------

try:
    height = int(input("Enter height: "))
    print("Choose Pattern (1-4):")
    pattern = int(input("Enter pattern number: "))

    if pattern == 1:
        for i in range(1, height + 1):
            for j in range(1, i + 1):
                print(j, end=" ")
            print()

    elif pattern == 2:
        for i in range(1, height + 1):
            for j in range(i):
                print(i, end=" ")
            print()

    elif pattern == 3:
        for i in range(height, 0, -1):
            for j in range(i, 0, -1):
                print(j, end=" ")
            print()

    elif pattern == 4:
        # Center pyramid pattern
        for i in range(1, height + 1):
            for space in range(height - i):
                print(" ", end="")
            for j in range(1, i + 1):
                print(j, end="")
            for j in range(i - 1, 0, -1):
                print(j, end="")
            print()

    else:
        print("Invalid pattern")

except:
    print("Invalid input")