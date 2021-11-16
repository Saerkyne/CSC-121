# Program: a03_conditionalLogic.py
# Author: Joel Hubbard
# Date: 8/21/2021
# Purpose: To parse an entered IP address, validate it, and determine its class

#Take input and set initial variables
#ip = input("Enter an IP address (xxx.xxx.xxx.xxx): ")
ip = "127.0.0.1"
ipClass = "None"

#Attempt to split on the period, also checks for the correct delimiter
count = 0
for char in ip:
    if char in ["."]:
        count += 1
if count != 3:
    print("Please use the correct delimiter.")
    exit()
else:   
    octets = ip.split('.')

    
#Check for the right number of octets
if (len(octets) != 4):
    print("IP addresses must have four groups of numbers, separated by three periods.")
    exit()
else:
    
#Pull each octet out for parsing
    first = octets[0]
    second = octets[1]
    third = octets[2]
    fourth = octets[3]
    
#Check for non-numerical values
    if (not first.isnumeric() or not second.isnumeric() or not third.isnumeric() or not fourth.isnumeric()):
        print("IP addresses are made of only numbers, delimited by periods.")
        exit()
        
#Redefine octets as integers instead of strings for final parsing 
    first = int(first)
    second = int(second)
    third = int(third)
    fourth = int(fourth)
    
#Check for the Class of the address, limited to classes A, B and C 
    if (first >= 0 and first <= 127):
        ipClass = "Class A"
    elif (first > 127 and first <= 191):
        ipClass = "Class B"
    elif (first > 191 and first <= 223):
        ipClass = "Class C"
    else:
        print("First octet is out of range. Must be a number between 0 and 223.")
        exit()
        
#Check for invalid values in the 2nd, 3rd, and 4th octets        
    if all(x < 0 for x in (second, third, fourth)) or all(x > 255 for x in (second, third, fourth)):
        print("Octet is out of IP range. All octets must be between 0 and 255.")
        exit()

#Successful entry of a valid IP. Return the Class of the address and exit. 
    else:
        print("IP address is valid. IP class is " + ipClass + ".")
        exit()
    