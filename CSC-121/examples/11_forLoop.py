#Program: 11_forLoop.py
#Author: Joel Hubbard
#Date: 8/22/2021
#Purpose: To demonstrate for loops

#Input and Variable Declaration
limit=int(input("Enter a Positive Whole Number: "))

#For loop to count to the limit, starting at one 
for count in range(1,limit + 1):
    print("Count equals " + str(count))

print("End of Loop")