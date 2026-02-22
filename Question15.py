# Program: Second largest number
# Description: Finds second largest element in a list

n = int(input())                   # number of elements
nums = []                          # list to store numbers

for i in range(n):                 # take input
    nums.append(int(input()))

largest = second = -999999         # initialize values

for num in nums:                   # find largest and second largest
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print(second)                      # display second largest