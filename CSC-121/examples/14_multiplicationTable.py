#Program: 14_multiplicationTable.py
#Author: Joel Hubbard
#Date: 8/22/2021
#Purpose: create a multiplication table of entered size

#Variable initialization
tableSize = int(input("Enter the size of the table: "))
decimal = "{:4d}"

#Column headings
col = 1
print("    ",end = "")
while col <= tableSize:
    print(decimal.format(col),end = "")
    col += 1
print("")

#Build table
row = 1
while row <= tableSize:
    col = 1
    #Row headings
    print(decimal.format(row),end = "")
    while col <= tableSize:
        ans = row * col
        print(decimal.format(ans),end = "")
        col += 1
    row += 1
    print("")

