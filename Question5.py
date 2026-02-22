# Program: Reverse string
# Description: Reverses the given string

try:
    text = input()                  # take string input
    rev = text[::-1]                # reverse string using slicing
    print(rev)                      # display reversed string

except:
    print("Invalid Input")          # handle error