#Program: 13_nestedForLoops.py
#Author: Joel Hubbard
#Date: 8/22/2021
#Purpose: To demonstrate nested for loops

#Variable initialization
limit = int(input("Enter a positive whole number: "))

#Nested for loops to count up to the limit
for count in range(0,limit):
    for count2 in range(0,limit):
        print(count, count2)
print("End of loop")