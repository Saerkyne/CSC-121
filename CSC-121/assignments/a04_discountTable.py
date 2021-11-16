#Program: a04_discountTable.py
#Author: Joel Hubbard
#Date: 8/22/2021
#Purpose: create a discount table, starting at an entered dollar value

#Variable initialization
dollarIn = int(input("Enter the starting whole dollar amount: "))
float = "{:6.2f}"

#Column headings
col = 1
#First column heading
print("|       ", end = "")
discount = 0.1
while col <= 9:
    print("|    ",end = "")
    print("{0:.0%}".format(discount), end = "")
    col += 1
    discount += 0.1
print("|")

#Build Table
row = 1
price = dollarIn
while row<= 20:
    col = 1
    #Row Headings
    discount = 0.1
    print("|",end = "")
    print("$" + float.format(price), end = "|")
    while col <= 9:
        ans = price - (price * discount)
        print("$" + float.format(ans),end = "|")
        col += 1
        discount += 0.1
    row += 1
    price += 0.5
    print("")