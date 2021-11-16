

# Filename: 20_avgGrades.py
# Author: Michael Souther
# Purpose: Read a file of space delimited grades and average them
# Read a space separated file.
# Parse and Store the contents in a list.
# Write the average to a file.

records = []
try:
   with open("grades.txt") as input_file:
       for line in input_file:
           parts = line.split(' ')
           name = parts[0]
           grade1 = parts[1]
           grade2 = parts[2]
           grade3 = parts[3]
           avg = (int(grade1) + int(grade2) + int(grade3)) / 3
           records.append([name, avg])
except FileNotFoundError as error:
      print("File Not Found; Try Again")
try:
   with open("avgs.txt",'w') as output_file:
       for record in records:
           output=record[0] +  " " + str(record[1]) + "\n"
           output_file.write(output)
except PermissionError as error:
      print("Permission Denied; Try Again")

