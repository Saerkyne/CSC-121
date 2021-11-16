# Filename: a10_csvReadWrite.py
# Author: Joel Hubbard
# Date: 10/16/2021
# Purpose: To read a csv file, calculate total production of each type of furniture,
#          calculate average prodution of each, and output to a separate csv file
import csv

# Read CSV into a list
finished = False
while not finished:
    try:
        filename = input("Enter the name of the Production input file: ")
        filePointer = open(filename,newline = '')
        reader = csv.reader(filePointer)
        data = []
        #skip header row
        next(reader)
        #put data in list
        for row in reader:
            chairs = int(row[2])
            tables = int(row[3])
            couches = int(row[4])
            recliners = int(row[5])
            data.append([chairs,tables,couches,recliners])
            length = len(data)
    except FileNotFoundError as error:
        print("File not found, try again.")
    else:
        finished = True
        filePointer.close()

# Total up each type of furniture and print the result

totals = list(map(sum, zip(*data)))

totalChairs = str(totals[0])
totalTables = str(totals[1])
totalCouches = str(totals[2])
totalRecliners = str(totals[3])

print("The total number of chairs is " + totalChairs + ".")
print("The total number of tables is " + totalTables + ".")
print("The total number of couches is " + totalCouches + ".")
print("The total number of recliners is " + totalRecliners + ".")

# Average the totals and print the result

avgChairs = str(round(totals[0]/length))
avgTables = str(round(totals[1]/length))
avgCouches = str(round(totals[2]/length))
avgRecliners = str(round(totals[3]/length))

print("The average number of chairs is " + avgChairs + ".")
print("The average number of tables is " + avgTables + ".")
print("The average number of couches is " + avgCouches + ".")
print("The average number of recliners is " + avgRecliners + ".")

# Output results into a CSV
finished = False
while not finished:
    try:
        filename = input("Enter the name of the Production Output File: ")
        filePointer = open(filename, 'w')
        writer = csv.writer(filePointer)
        writer.writerow(["Chairs","Tables","Couches","Recliners"])
        writer.writerow([totalChairs,totalTables,totalCouches,totalRecliners])
        writer.writerow([avgChairs,avgTables,avgCouches,avgRecliners])
    except PermissionError as error:
        print("Permission error, try again.")
    else:
        finished = True
        filePointer.close()