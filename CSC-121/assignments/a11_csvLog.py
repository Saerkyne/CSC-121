# Filename: a11_csvLog.py
# Author: Joel Hubbard
# Date: 10-22-2021
""" Purpose: Create a program to read and write a csv for egg production.  
The program should read in the csv and calculate the total production of 
eggs.   It could also calculate average production eggs per house.   It should 
output the production figures to a summary csv file. Add a logger to keep 
track of when the program starts(info).  If the csv can't be read or summary 
can't be written log a critical level error. If the house does not contain
the production number write a warning. 

House, Number_Of_Eggs
House_1, 1002
House_2, 1210
House_3,
House_4, 1410
House_5, 1121

Test to perform.

    Try to read a file that does not exist.
    Change the permissions one the output file to prevent writing.
    touch filename
    chmod 000 filename """

import logging, csv

# Log Format

LOG_ENTRY="%(levelname)s %(asctime)s %(message)s"

# Note: That logging is set to debug. Normally it would be set to a warning or error. 
logging.basicConfig(filename="eggs.log",
                    format=LOG_ENTRY,
                    filemode='w',
                    level=logging.DEBUG)

logger=logging.getLogger()

logger.debug("Program Start")
finished = False
while not finished:
    try:
        filename = input("Enter the name of the Egg input file: ")
        filePointer = open(filename,newline = '')
        reader = csv.reader(filePointer)
        data = []
        #skip header row
        next(reader)
        #put data in list
        count = 0
        for row in reader:
            count += 1
            logger.debug("Reading in row number " + str(count))
            house = row[0]
            eggs = row[1].strip()
            data.append(eggs)
        eggCount = 0
        intData = []
        for item in data:
            eggCount += 1
            try:
                item = int(item)
                intData.append(item)
                logger.debug("Added integer from index " + str(eggCount))
            except:
                logger.warning("No data at index " + str(eggCount))
                intData.append(0)
        logger.debug("All data read in.")
        print(intData)
    except FileNotFoundError as error:
        print("File not found, try again.")
        logger.critical("CSV cannot be read.")
        exit()
    else:
        finished = True
        filePointer.close()

prodTotal = sum(intData)
logger.debug("Calculating Total Production")
prodAvg = (sum(intData))/len(intData)
logger.debug("Calculating Average Production")


# Output results
finished = False
while not finished:
    try:
        filename = input("Enter the name of the output file: ")
        logger.debug("Writing results to CSV")
        filePointer = open(filename, 'w')
        writer = csv.writer(filePointer)
        writer.writerow(["Total","Average"])
        writer.writerow([prodTotal,prodAvg])
    except PermissionError as error:
        print("Permission error, try again.")
        logger.critical("Permission error.")
    else:
        finished = True
        filePointer.close()