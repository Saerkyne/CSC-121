# Program: 08_stringMethods.py
# Author: Joel Hubbard
# Date: 8/21/2021
# Purpose: To demonstrate string assignment and methods

phone="336-838-6478"

print(phone)
print("First digit in phone number", phone[0])
print("Area Code: ", phone[0:3])
print("Remove dashes: ",phone.replace('-',''))
print("Length of phone number: ", len(phone))
print("Split at dashes: ",phone.split('-'))


# Part 2
# Purpose: The Demo String method. Validate a stock symbol.
# For our stock symbol all character must be alphabetic and uppercase.
# It can have a minimum of 1 character and a max of 4 characters.

symbol=input('Enter a stock symbol: ')

valid=True

if (len(symbol) < 1): 
    valid=False

if (len(symbol) > 4):
    valid=False

if (not symbol.isalpha()) or (not symbol.isupper()):
    valid=False

if (valid):
    print(symbol,'is a valid stock symbol.')
else:
    print(symbol,'is not a valid stock symbol.')