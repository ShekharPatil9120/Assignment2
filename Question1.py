# ---------------------------------------------------
# Question 1: Personal Bio Card
# Display student details in a formatted box
# Requirements:
# - Use variables
# - Show output inside a box
# - Make it look neat
# ---------------------------------------------------

# Student details (you can change these values)
name = "Shekhar Patil"
age = 22
course = "Python Programming"
college = "CMRIT College"
email = "shekharpatil9120@gmail.com"

# Box width
width = 40

# Top border
print("╔" + "═" * width + "╗")

# Title
title = "STUDENT BIO CARD"
print("║" + title.center(width) + "║")

# Divider
print("╠" + "═" * width + "╣")

# Details
print("║ " + f"Name   : {name}".ljust(width - 1) + "║")
print("║ " + f"Age    : {age} years".ljust(width - 1) + "║")
print("║ " + f"Course : {course}".ljust(width - 1) + "║")
print("║ " + f"College: {college}".ljust(width - 1) + "║")
print("║ " + f"Email  : {email}".ljust(width - 1) + "║")

# Bottom border
print("╚" + "═" * width + "╝")