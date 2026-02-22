# Program: Palindrome checker
# Description: Checks whether the input string is palindrome

def check_palindrome(text):
    text = text.strip().lower()
    return text == text[::-1]

try:
    user_input = input()
    if check_palindrome(user_input):
        print("Palindrome")
    else:
        print("Not Palindrome")
except:
    print("Invalid Input")