#  Program: a07_schoolDict.py
#  Author: Joel Hubbard
#  Date: 09/26/2021
#  Purpose: Manage a dictionary

"""
Create an app that maintains dictionary of High Schools.
The app should have a list of Wilkes County High Schools
where the key in the initials and the value is the full name.
For Example NWHS is North Wilkes High School.  Create a menu
items that allows you to add or delete an entry from the
dictionary.  Create a menu item that display the key value pairs
one per line.  The menu should have the option to exit/quit.
"""
import time

schoolDict = {"WCHS" : "Wilkes Central High School",
              "NWHS" : "North Wilkes High School"}

finished = False

while not finished:
    print("School Dictionary")
    print("1. Add School")
    print("2. Remove School")
    print("3. Display Key/Value Pairs")
    print("4. Exit")
    
    selection = input("Enter a selection: ")
    
    if selection == "1":
        print()
        print("Add School to Dictionary")
        schoolKey = input("Enter the initials of the school: ")
        schoolName = input("Enter the full name of the school: ")
        
        schoolDict[schoolKey] = schoolName
        
    
    if selection == "2":
        print()
        print("Remove School from Dictionary")
        for key,value in schoolDict.items():
            print("Key: " + key + ", Value: " + value)
        print()
        schoolKey = input("Enter the Key of the school to remove: ")
        print(schoolKey)
        del schoolDict[schoolKey]
    
    if selection == "3":
        print()
        print("Display Dictionary")
        
        for key,value in schoolDict.items():
            print("Key: " + key + ", Value: " + value)
        print()
        time.sleep(3)
            
    
    if selection == "4":
        finished = True