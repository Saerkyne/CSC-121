

# Author: Michael Souther
# Filename: 27_bin_to_dec.py
# Purpose: Convert a binary number into a decimal number
def binary_to_decimal(binary):
   if len(binary) == 1:
      return int(binary)
   else:
      first_digit=binary[0:1]
      print("first digit", first_digit)
      remain_digits=binary[1:len(binary)]
      print("remain digits", remain_digits)
      result=int(first_digit) * 2**(len(binary)-1)
      print("result", result)
      return binary_to_decimal(remain_digits) + result

#print(binary_to_decimal('11111111'))
result = ''


def binToDec(binary):
    if len(binary) == 1:
        return int(binary)
    else:
        firstDigit = binary[0:1]
        remainder = binary[1:len(binary)]
        result = int(firstDigit) * 2**(len(binary) - 1)
        return binToDec(remainder) + result

def decToOct(decimal):
   
   while decimal >= 8:
      remainder = decimal % 8
      print(remainder)
      decimal = decimal // 8
      print(decimal)
      result = str(remainder).append(str(decimal))
      print(result)

print(decToOct(31))