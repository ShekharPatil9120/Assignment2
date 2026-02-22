# Program: Count vowels
# Description: Counts number of vowels in a string

try:
    text = input().lower()          # take input and convert to lowercase
    count = 0                       # initialize counter

    for ch in text:                 # loop through each character
        if ch in "aeiou":           # check if vowel
            count += 1              # increase count

    print(count)                    # display result

except:
    print("Invalid Input")          # handle error