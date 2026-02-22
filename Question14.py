# Program: Character frequency
# Description: Counts frequency of each character in a string

text = input()                     # take string input
freq = {}                          # dictionary to store count

for ch in text:                    # loop through characters
    if ch in freq:                 # if already present
        freq[ch] += 1
    else:
        freq[ch] = 1               # add new character

for key in freq:                   # print character counts
    print(key, freq[key])