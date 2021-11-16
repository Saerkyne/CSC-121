

# Filename: 21_grades_csv.py
# Author: Michael Souther
# Date: 10/2/2019
# Purpose: To read a grade2.csv file, calculate an average and write the average
#          and student id to a file.
# Read comma separated values from a file.
# Write comma separated values to a file.
import csv
# Read csv and store it in a list
finished=False
while not finished:
   try:
      filename=input("Enter the name of the Grades input file: ")
      file_pointer=open(filename,newline='')
      reader = csv.reader(file_pointer)
      headings = next(reader)
      data=[]
      for row in reader:
         student_id=row[2]
         grade1=int(row[3])
         grade2=int(row[4])
         grade3=int(row[5])
         data.append([student_id,grade1,grade2,grade3])
   except FileNotFoundError as error:
      print("File Not Found; Try Again")
   else:
      finished=True
      file_pointer.close()

# Calculate the Student Averages and Store it in a list
output_data=[]
for student in data:
   student_id=student[0]
   grade1=student[1]
   grade2=student[2]
   grade3=student[3]
   average=round((grade1 + grade2 + grade3)/3,1)
   output_data.append([student_id,average])

# Write the second out as a csv
finished=False
while not finished:
   try:
      filename=input("Enter the name of the Grades Output file: ")
      file_pointer=open(filename,'w')
      writer = csv.writer(file_pointer)
      writer.writerow(["Student_ID","Average"])
      for student in output_data:
         writer.writerow([student[0],student[1]])
   except PermissionError as error:
      print("Permission Error; Try Again")
   else:
      finished=True
      file_pointer.close()

