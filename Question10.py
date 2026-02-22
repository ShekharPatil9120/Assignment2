# Program: Word count
# Description: Counts number of words in a sentence

text = input()                # take sentence input
words = text.split()          # split into words
count = len(words)            # count words
print(count)                  # display result