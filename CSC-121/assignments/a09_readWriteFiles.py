# Filename: a09_readWriteFiles.py
# Author: Joel Hubbard
# Date: 10/12/2021
# Purpose: To read a phones.csv file, add or remove a listing, 
#          and write the file back out
import csv

# Read csv and store it in a list
finished = False
while not finished:
    try:
        filename = input("Enter the name of the phone listing input file: ")
        filePointer = open(filename, newline = '')
        reader = csv.reader(filePointer)
        headings = next(reader)
        data = []
        for row in reader:
            phoneNumber = row[0]
            firstName = row[1]
            lastName = row[2]
            data.append([phoneNumber, firstName, lastName])
    except FileNotFoundError as error:
        print("File Not Found; Try Again")
    
    else:   
        finished = True
        filePointer.close()

print(data)
#Open menu for adding or removing rows
finished = False
while not finished:
    print("Phone Listing Editor")
    print("1. Add a Number")
    print("2. Delete a Number")
    print("3. Exit")

    selection = input("Enter a selection: ")

    if selection == "1":
        #Get inputs from user and create list
        
        pNumber = input("Enter a phone number (XXX-XXX-XXXX): ")
        
        fName = input("Enter a first name: ")
       
        lName = input("Enter a last name: ")
        
        data.append([pNumber, fName, lName])
        

        #Try to write the file
        try:
            file = open(filename, 'w')
            writer = csv.writer(file)
            writer.writerow(["Number", "First Name", "Last Name"])
            for number in data:
                writer.writerow([number[0],number[1],number[2]])

        except PermissionError as error:
            print("Permission Error; Try Again")
        
        else:
            file.close()

        

    if selection == "2":
        print()
        print(data)
        print()
        delNum = input("Enter the number of the entry to delete: ")

        if delNum not in data:
            print("Number not found, try again.")

        else:
        
            try:
                file = open(filename, 'w')
                writer = csv.writer(file)
                writer.writerow(["Number", "First Name", "Last Name"])
                for number in data:
                    if number[0] != delNum:
                        writer.writerow(number)

                print(delNum + " has been deleted.")
            except PermissionError as error:
                print("Permission Denied, Try Again")
            
            else:
                file.close()


    if selection == "3":
        finished = True