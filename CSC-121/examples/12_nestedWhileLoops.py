#Program: 12_nestedWhileLoops.py
#Author: Joel Hubbard
#Date 8/22/2021
#Purpose: To demonstrate nested while loops

#Variable initialization
count = 0
limit = int(input("Enter a Positive Whole Number: "))

#While loops to maintain two counts, 
while count < limit:
    count2=0
    while count2 < limit:
        print(count, count2)
        count2 += 1
    count += 1

print("End of Loops")