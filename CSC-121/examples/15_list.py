# Program: listDemo.py
# Author: Michael Souther
# Date: 09/09/2019
# Purpose: Demo List
finished=False
phoneList=["Smith, John 336-838-5555",
           "Doe, Jane 336-838-5556",
           "Adams, Bill 336-838-1111"]
while not finished:
    print("Phone List")
    print("1. Add Phone Listing")
    print("2. Remove Phone Listing")
    print("3. Sort Phone Listings")
    print("4. Reverse List")
    print("5. Clear List")
    print("6. Phone List Length")
    print("7. Display Phone List")
    print("8. Quit")
    selection=input("Enter selection: ")
    if selection == "1":
        listing=input("Enter listing (Smith, John 336-838-5555): ")
        phoneList.append(listing)
    if selection == "2":
        count=0
        print("Remove Phone Listing")
        for listing in phoneList:
            print(str(count)," ",listing)
            count=count + 1
        index=input("Enter the number of the phone listing to remove: ")
        phoneList.pop(int(index))
    if selection == "3":
        phoneList.sort()
        count=0
        print()
        print("Sorted Phone Listing")
        for listing in phoneList:
            print(str(count)," ",listing)
            count=count + 1
        print()
    if selection == "4":
        phoneList.reverse()
        count=0
        print()
        print("Sorted Reverse Order Phone Listing")
        for listing in phoneList:
            print(str(count)," ",listing)
            count=count + 1
        print()
    if selection == "5":
        phoneList.clear()
        count=0
        print()
        print("Phone Listing after clear")
        for listing in phoneList:
            print(str(count)," ",listing)
            count=count + 1
        print()
    if selection == "6":
        length=len(phoneList)
        print()
        print("Phone Listing length is: ", str(length))
        print()
    if selection == "7":
        count=0
        print()
        print("Phone Listing")
        for listing in phoneList:
            print(str(count)," ",listing)
            count=count + 1
        print()
    if selection == "8":
        finished = True