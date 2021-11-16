# Program: a02_stringFunctions.py
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

codeSeparated = codeIn.split(':')

codeAlpha = codeSeparated[0]
codeNumOne = codeSeparated[1]
codeNumTwo = codeSeparated[2]


if (not codeAlpha.isalpha()) or (not codeAlpha.isupper()):
    print("Entered Alphabetic Section not alpha/not uppercase")
    exit()

if (not codeNumOne.isnumeric()) or (not codeNumTwo.isnumeric()):
    print("Entered Numeric Section is not numeric")
    exit()

else:
    print("Entered code is valid.")