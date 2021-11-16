# Program: a02_stringFunctions_V2.py
# Author: Joel Hubbard
# Date: 8/21/2021
# Purpose: To validate a product code with format AAA:##:######

codeIn = input("Enter the product code, with colon separators (AAA:##:######): ")

if (len(codeIn) < 13) or (len(codeIn) >= 14):
    print("Entered Code Incorrect Length")
    exit()

if (codeIn[3] != ":") or (codeIn[6] != ":"):
    print("Please use a colon delimiter.")
    exit()

codeAlpha = codeIn[0:3]
codeNumOne = codeIn[4:6]
codeNumTwo = codeIn[7:13]


if (not codeAlpha.isalpha()) or (not codeAlpha.isupper()):
    print("Entered Alphabetic Section not alpha/not uppercase")
    exit()

if (not codeNumOne.isnumeric()) or (not codeNumTwo.isnumeric()):
    print("Entered Numeric Section is not numeric")
    exit()

else:
    print("Entered code is valid.")