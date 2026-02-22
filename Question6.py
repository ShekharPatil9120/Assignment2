# ---------------------------------------------------
# Question 6: Grade Calculator
# Take marks of 5 subjects (out of 100)
# Display total, percentage, grade and pass/fail
# Pass if all subjects >= 40
# ---------------------------------------------------

try:
    marks = []
    total = 0
    pass_status = True

    # Taking marks
    for i in range(1, 6):
        m = float(input(f"Enter marks for subject {i}: "))
        marks.append(m)
        total += m
        if m < 40:
            pass_status = False

    percentage = total / 5

    # Grade calculation
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n--- Result ---")
    print("Total Marks:", total)
    print("Percentage:", percentage)
    print("Grade:", grade)

    if pass_status:
        print("Result: PASS")
    else:
        print("Result: FAIL")

except:
    print("Invalid input")