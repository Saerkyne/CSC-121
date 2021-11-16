#Program: a08_functions.py
#Author: Joel Hubbard
#Date: 10/02/2021
#Purpose: Create a menu driven program to calculate 
#         the conversion of temperatures between Celsius, Kelvin, 
#         Fahrenheit.  Create function for each possible conversion.
import time

finished = False

TfC = lambda c : int(((9/5) * int(c)) + 32)
TcF = lambda f : int((5/9) * (int(f) -32))
TcK = lambda k : int(k) - 273
TkC = lambda c : int(c) + 273

def CtoF(Celcius): 
    return TfC(Celcius)

def CtoK(Celcius):
    return TkC(Celcius)

def FtoK(Fahrenheit):
    Celcius = TcF(Fahrenheit)
    return TkC(Celcius)

def FtoC(Fahrenheit):
    return TcF(Fahrenheit)

def KtoC(Kelvin):
    return TcK(Kelvin)

def KtoF(Kelvin):
    Celcius = TcK(Kelvin)
    return TfC(Celcius)

while not finished:
    print("Temperature Converter")
    print("1. Celcius to Fahrenheit")
    print("2. Celcius to Kelvin")
    print("3. Fahrenheit to Celcius")
    print("4. Fahrenheit to Kelvin")
    print("5. Kelvin to Celcius")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")
    print()

    selection = input("Enter a selection: ")
    print()

    if selection == "1":
        temp = input("Enter a Temperature value (Integers only): ")
        print()
        
        print(str(temp) + " degrees Celcius is equal to " + str(CtoF(temp)) + " degrees Fahrenheit.")
        print()
        time.sleep(3)

    if selection == "2":
        temp = input("Enter a Temperature value (Integers only): ")
        print()
        
        print(str(temp) + " degrees Celcius is equal to " + str(CtoK(temp)) + " degrees Kelvin.")
        print()
        time.sleep(3)
    
    if selection == "3":
        temp = input("Enter a Temperature value (Integers only): ")
        print()
        
        print(str(temp) + " degrees Fahrenheit is equal to " + str(FtoC(temp)) + " degrees Celcius.")
        print()
        time.sleep(3)
    
    if selection == "4":
        temp = input("Enter a Temperature value (Integers only): ")
        print()
        
        print(str(temp) + " degrees Fahrenheit is equal to " + str(FtoK(temp)) + " degrees Kelvin.")
        print()
        time.sleep(3)
    
    if selection == "5":
        temp = input("Enter a Temperature value (Integers only): ")
        print()
        
        print(str(temp) + " degrees Kelvin is equal to " + str(KtoC(temp)) + " degrees Celcius.")
        print()
        time.sleep(3)
    
    if selection == "6":
        temp = input("Enter a Temperature value (Integers only): ")
        print()
        
        print(str(temp) + " degrees Kelvin is equal to " + str(KtoF(temp)) + " degrees Fahrenheit.")
        print()
        time.sleep(3)
    
    if selection == "7":
        finished = True