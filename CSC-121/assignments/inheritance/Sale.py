# Filename: Sale.py
# Date: 11.14.2021
# Author: Joel Hubbard
# Purpose: 
"""
Create a class named Sale.  The Sale class should have 2 attributes the name and the price. 
A Sale object should be created with both attributes. The Sale class should have set and get
 methods for each of the attributes. The Sale class should have a string method to output a sale in standard form.   
"""

class Sale(object):
    def __init__(self, name, price):
        # Initialize two attributes
        self.name = name
        self.price = price
    
    def __str__(self):
        # print return in standard form
        return "Item: " + str(self.name) + ", Price: $" + str(self.price)

    def getName(self):
        return self.name
    
    def getPrice(self):
        return self.price
    
    def setName(self, newName):
        self.name = newName
    
    def setPrice(self, newPrice):
        self.price = newPrice
