# ---------------------------------------------------
# Question 13: Sum, Average, Max, Min
# Bonus: Median and Mode

numbers.sort()

# Median
if count % 2 == 1:
    median = numbers[count // 2]
else:
    median = (numbers[count//2 - 1] + numbers[count//2]) / 2

# Mode
frequency = {}
for num in numbers:
    frequency[num] = frequency.get(num, 0) + 1

mode = max(frequency, key=frequency.get)

print("Median:", median)
print("Mode:", mode)