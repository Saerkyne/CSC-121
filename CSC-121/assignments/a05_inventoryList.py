#  Program: a05_inventoryList.py
#  Author: Joel Hubbard
#  Date: 09/20/2021
#  Purpose: Maintain an inventory list

finished=False

itemDict = {2: ["ASUS Laptop", "Home"],
            1: ["Dell Laptop", "Work"],
            3: ["MSI Laptop", "Coffee Shop"]}

while not finished:
    print("Inventory List")
    print("1. Add Item Listing")
    print("2. Remove Item Listing")
    print("3. Sort Item Listings")
    print("4. Reverse List")
    print("5. Clear List")
    print("6. Display Item List")
    print("7. Quit")
    
    selection=input("Enter selection: ")
    
    if selection == "1":
        listing=input("Enter listing (itemID:itemName:itemLocation): ")
        
        dictList = listing.split(':')
        itemID = int(dictList[0])
        itemName = dictList[1]
        itemLocation = dictList[2]
        
        itemDict[itemID]  = [itemName, itemLocation]
        
        
    if selection == "2":
        count=0
        print("Remove Item Listing")
        for key,value in itemDict.items():
            valueName = value[0]
            valueLoc = value[1]
            print(str(count)," ",key, ":", valueName, ":", valueLoc)
            count=count + 1
        itemRemove=int(input("Enter the item number of the item to remove: "))
        
        for index, key in enumerate(itemDict):
            if index == itemRemove:
                del itemDict[key]
                break
            
    if selection == "3":
        sortedDict = dict(sorted(itemDict.items(), key = lambda item: item[0]))
            
        count = 0
        print()
        print("Sorted Item Listing")
        for key,value in sortedDict.items():
            valueName = value[0]
            valueLoc = value[1]
            print(str(count)," ",key, ":", valueName, ":", valueLoc)
            count=count + 1
        print()
        
    if selection == "4":
        reversedDict = dict(reversed(sorted(itemDict.items(), key = lambda item: item[0])))
            
        count=0
        print()
        print("Sorted Reverse Order Item Listing")
        for key,value in reversedDict.items():
            valueName = value[0]
            valueLoc = value[1]
            print(str(count)," ",key, ":", valueName, ":", valueLoc)
            count=count + 1
        print()
        
    if selection == "5":
        itemDict.clear()
        count=0
        print()
        print("Item Listing after clear")
        for key,value in itemDict.items():
            valueName = value[0]
            valueLoc = value[1]
            print(str(count)," ",key, ":", valueName, ":", valueLoc)
            count=count + 1
        print()
        
    if selection == "6":
        count=0
        print()
        print("Item Listing")
        for key,value in itemDict.items():
            valueName = value[0]
            valueLoc = value[1]
            print(str(count)," ",key, ":", valueName, ":", valueLoc)
            count=count + 1
        print()
        
    if selection == "7":
        finished = True