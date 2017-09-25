from fractions import Fraction

max_sum = 0

for a in range(0,100):
    for b in range(0,100):
        total = 0
        for digit in str(a**b):
            total += int(digit)
        if total > max_sum:
            max_sum = total


print(max_sum)

