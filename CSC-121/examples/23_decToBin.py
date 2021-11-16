

# Author: Michael Souther
# Filename: 25_dec_to_bin.py
# Purpose: Convert a decimal number into a binary number
def decimal_to_binary(decimal):
   if decimal <= 1:
      return str(decimal)
   else:
      return decimal_to_binary(decimal//2) + str(decimal%2)

print(decimal_to_binary(9))
print(decimal_to_binary(255))

