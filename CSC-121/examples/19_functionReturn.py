

#  Program: 19_function_return.py
#  Author: Michael Souther
#  Date: 09/28/2020
#  Create a function to return the calculated MPG
def mpg(miles,gallons):
    """Function to return the MPG given miles and gallons"""
    mpgVal = miles / gallons
    return mpgVal

miles=float(input("Enter the miles traveled: "))
gallons=float(input("Enter the gallons used: "))
currMPG=mpg(miles,gallons)
print("The MPG for a trip of ", miles, " miles and ", gallons, " gallons is ", currMPG)