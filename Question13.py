# Program: Remove duplicates
# Description: Removes duplicate elements from a list

n = int(input())                   # number of elements
nums = []                          # list to store input

for i in range(n):                 # take list input
    nums.append(int(input()))

unique = []                        # list for unique elements

for num in nums:                   # check each element
    if num not in unique:          # if not already present
        unique.append(num)

for val in unique:                 # print unique elements
    print(val)