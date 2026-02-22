# Program: Anagram check
# Description: Checks if two strings are anagrams

s1 = input().replace(" ", "").lower()      # first string
s2 = input().replace(" ", "").lower()      # second string

if sorted(s1) == sorted(s2):               # compare sorted characters
    print("Anagram")
else:
    print("Not Anagram")