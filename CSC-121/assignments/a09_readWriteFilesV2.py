# Filename: a09_readWriteFilesV2.py
# Author: Joel Hubbard
# Date: 10/12/2021
# Purpose: To read a phones.txt file, add or remove a listing, 
#          and write the file back out.
records = []


#Open menu for adding or removing rows
finished = False
while not finished:
    print("Phone Listing Editor")
    print("1. Add a Number")
    print("2. Delete a Number")
    print("3. Exit")

    selection = input("Enter a selection: ")

    if selection == "1":
        #Open the file for editing
        try:
            with open("phones.txt") as inputFile:
                for _ in range(1):
                    next(inputFile)
                try:
                    for line in inputFile:
                        line = line.strip("\n")
                        parts = line.split(' ')
                        pNumber = parts[0]
                        fName = parts[1]
                        lName = parts[2]
                        records.append([pNumber, fName, lName])
                except:
                    print("Error")
        except FileNotFoundError as error:
            print("File not found; try again.")
            exit()

        #Get inputs from user and create list
        data = []
        pNumber = input("Enter a phone number (XXX-XXX-XXXX): ")
        
        fName = input("Enter a first name: ")
       
        lName = input("Enter a last name: ")
        
        data.append([pNumber, fName, lName])
        

        #Try to write the file
        try:
            with open("phones.txt", 'w') as outputFile:
                outputFile.write("Phone Number Listing")
                for number in data:
                    outputData = "\n" + number[0] + " " + number[1] + " " + number[2]
                    outputFile.write(outputData)
                for number in records:
                    output = "\n" + number[0] + " " + number[1] + " " + number[2]
                    outputFile.write(output)
                
                    
                    
        except PermissionError as error:
            print("Permission Error; Try Again")
        
               

    if selection == "2":
        print()
        #Open the file for editing
        try:
            with open("phones.txt") as inputFile:
                for _ in range(1):
                    next(inputFile)
                for line in inputFile:
                    line = line.strip("\n")
                    parts = line.split(' ')
                    pNumber = parts[0]
                    fName = parts[1]
                    lName = parts[2]
                    records.append([pNumber, fName, lName])
        except FileNotFoundError as error:
            print("File not found; try again.")
            exit()
        print(records)
        print()
        delNum = input("Enter the number of the entry to delete: ")


        for sublist in records:
            if sublist[0] == delNum:
                print("Number found.")
                try:
                    records.remove(sublist)

                except PermissionError as error:
                    print("Permission denied, try again.")
                with open("phones.txt", 'w') as outputFile:
                    outputFile.write("Phone Number Listing")
                    for x in records:
                        output = "\n" + x[0] + " " + x[1] + " " + x[2]  
                        outputFile.write(output)
                        
        

    if selection == "3":
        outputFile.close()
        finished = True