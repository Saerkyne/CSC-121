# Filename: SalesTest.py
# Author: Joel Hubbard
# Date: 17.11.2021

from DiscountSale import *

# Variable Declaration
itemName = input("Enter an Item: ")
itemPrice = input("Enter the Price: ")
itemDiscount = input("Enter the Discount percentage (if no discount, enter 0): ")

# Creation of discount object
discount = DiscountSale(itemName, itemPrice, itemDiscount)

# Print variables before calculation
print(discount)

# Print discounted price
print(discount.calcDiscount())

# Set new item name using inherited method and recalculate
newName = input("Enter a new Item: ")
discount.setName(newName)
print(discount.calcDiscount())

# Set new price using inherited method and recalculate
newPrice = input("Enter a new Price: ")
discount.setPrice(newPrice)
print(discount.calcDiscount())

# Set new discount rate using local method and recalculate
newDiscount = input("Enter a new Discount: ")
discount.setDiscount(newDiscount)
print(discount.calcDiscount())

# Creation of basic Sale object
sale = Sale(newName, newPrice)

# Print variable in basic object
print(sale)
