# Filename: a12_recursion.py
# Author: Joel Hubbard
# Date: 10-22-2021
""" Purpose: Create a program to convert a number from binary, decimal, or octal to
binary, decimal, or octal.  The program should be menu driven.  The program should 
allow the user to enter a number, it's base and the convert to base.  The program should then convert 
to the new base and display the results. 

Octal 0 - 7
"""
import time
# Define functions for the conversions

# Binary Conversions
def binToDec(binary):
    if len(binary) == 1:
        return int(binary)
    else: 
        firstDigit = binary[0:1]
        remainder = binary[1:len(binary)]
        result = int(firstDigit) * 2**(len(binary) - 1)
        return binToDec(remainder) + result

def binToOct(binary):
    decimal = binToDec(binary)
    octal = decToOct(decimal)
    return octal
    

# Decimal Conversions
def decToBin(decimal):
    if decimal == 0:
        binary = 0
    else:
        binary = decimal % 2 + 10 * (decToBin(decimal // 2))
    return binary



def decToOct(decimal):
    if decimal != 0:
        decToOct(decimal // 8)
        print(decimal % 8, end='')
        

# Octal Conversions

def octToBin(octal):
    decimal = octToDec(octal, 0)
    binary = decToBin(decimal)
    return binary

def octToDec(octal, i):
    if octal >= 0 and octal <= 7:
        return octal*pow(8, i)
    
    lastDigit = octal % 10
    return (pow(8, i) * lastDigit) + octToDec(octal // 10, i + 1)


# Create the base menu
finished = False
while not finished:
    print("Base Conversions")
    print()
    print("1. Convert from Binary")
    print("2. Convert from Decimal")
    print("3. Convert from Octal")
    print("4. Exit")
    print()
    
    selection = input("Enter a selection: ")
# check for the selection
    if selection == '1':
        internalFinished = False
        while not internalFinished:
            print()
            print("Binary Conversion")
            print()
            print("1. Convert to Decimal")
            print("2. Convert to Octal")
            print("3. Exit")
            print()

            selection = input("Enter a selection: ")
            print()
            
            if selection == '1':
                # Binary to Decimal
                numIn = input("Enter a binary number: ")
                print("Converting Binary to Decimal")
                time.sleep(3)
                numOut = binToDec(numIn)
                print(numOut)
                time.sleep(3)

            if selection == '2':
                # Binary to Octal
                numIn = input("Enter a binary number: ")
                print("Converting Binary to Octal")
                time.sleep(3)
                binToOct(numIn)
                time.sleep(3)

            if selection == '3':
                internalFinished = True
                
    
    elif selection == '2':
        internalFinished = False
        while not internalFinished:
            print()
            print("Decimal Conversion")
            print()
            print("1. Convert to Binary")
            print("2. Convert to Octal")
            print("3. Exit")
            print()

            selection = input("Enter a selection: ")
            print()
            
            if selection == '1':
                # Decimal to Binary
                numIn = input("Enter a decimal number: ")
                print("Converting Decimal to Binary")
                time.sleep(3)
                numOut = decToBin(int(numIn))
                print(numOut)
                time.sleep(3)

            if selection == '2':
                # Decimal to Octal
                numIn = input("Enter a decimal number: ")
                print("Converting Decimal to Octal")
                time.sleep(3)
                decToOct(int(numIn))
                time.sleep(3)

            if selection == '3':
                internalFinished = True
                
    
    elif selection == '3':
        internalFinished = False
        while not internalFinished:
            print()
            print("Octal Conversion")
            print()
            print("1. Convert to Binary")
            print("2. Convert to Decimal")
            print("3. Exit")
            print()

            selection = input("Enter a selection: ")
            print()
            
            if selection == '1':
                # Octal to Binary
                numIn = input("Enter an octal number: ")
                print("Converting Octal to Binary")
                time.sleep(3)
                numOut = octToBin(int(numIn))
                print(numOut)
                time.sleep(3)

            if selection == '2':
                # Octal to Decimal
                numIn = input("Enter an octal number: ")
                print("Converting Octal to Decimal")
                time.sleep(3)
                numOut = octToDec(int(numIn), 0)
                print(numOut)
                time.sleep(3)

            if selection == '3':
                internalFinished = True
                
    
    elif selection == '4':
        finished = True
        
    
    else:
        print("You must select an option from the list.")


