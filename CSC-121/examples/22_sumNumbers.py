

# Author: Michael Souther
# Filename: 24_sum_numbers.py
# Purpose: Is to sum the numbers between 1 and some limit
def sum_numbers(value):
   if value == 1:
      return value
   else:
      return sum_numbers(value - 1) + value

print(sum_numbers(10))
print(sum_numbers(100))

