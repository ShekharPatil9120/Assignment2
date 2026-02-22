# Program: Count even numbers
# Description: Counts even numbers from 1 to n

n = int(input())              # take input
count = 0                     # initialize counter

for i in range(1, n + 1):     # loop from 1 to n
    if i % 2 == 0:            # check even
        count += 1            # increase count

print(count)                  # display result