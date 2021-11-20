# Filename: DiscountSale.py
# Date: 11.20.2021
# Author: Joel Hubbard
# Purpose: 
"""
Create a class named DiscountSale.  A Discount Sale will inherit all the attributes of a Sale. 
A Discount Sale will have 3 attributes the name, the price, and the discount rate. A Discount 
Sale object should be created with all 3 attributes. The Discount Sale class should have a set 
and get method for the discount rate. The Discount Sale class should include a string method to 
output the discount sale in standard form.  Create a Python program to ask the user to enter the 
attributes for a standard Sale and for a Discount Sale. Create instances of both objects and test 
each of the methods for that object.
"""
from Sale import *

class DiscountSale(Sale):
    def __init__(self, name, price, discountRate):
        super().__init__(name, price)
        self.discountRate = int(discountRate)
    
    def __str__(self):
        return "Item: " + str(self.name) + ", pre-Discount Price: $" + str(self.price) + ", Discount: " + str(self.discountRate) + "%"

    def getDiscount(self):
        return self.discountRate

    def setDiscount(self, newRate):
        self.discountRate = int(newRate)

    def calcDiscount(self):
        if self.discountRate == 0:
            return "No discount"
        
        else:
            discountRate = self.discountRate / 100
            discountAmount = self.price * discountRate
            discountPrice = self.price - discountAmount
            return "Item: " + str(self.name) + ", Discount Price: $" + str(discountPrice) + ", Discount: " + str(self.discountRate) + "%"
