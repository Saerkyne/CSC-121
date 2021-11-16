#  Program: a06_setManagement.py
#  Author: Joel Hubbard
#  Date: 09/26/2021
#  Purpose: Manage a set

"""
Create an app that maintains sets of blacklisted and whitelisted
websites.   The app should be able to add or delete sites from
either set.  The app should be able to display one of the sets
or all unique items in both sets.   It should also be able to
display the items the sets have in common.
"""
import time

finished = False
whitelist = {"google.com", "youtube.com", "wilkescc.edu"}
blacklist = {"badsite.org", "badsite.com", "wilkescc.edu"}

while not finished:
    print("Website Filtering")
    print("1. Display Whitelist")
    print("2. Display Blacklist")
    print("3. Add a site")
    print("4. Remove a site")
    print("5. Display common sites")
    print("6. Display unique sites (Single List)")
    print("7. Display unique sites (by list)")
    print("8. Exit")
    print()
    
    selection = input("Enter a selection: ")
    
    if selection == "1":
        print()
        print("Website Whitelist")
        count = 1
        for item in whitelist:
            print(str(count) + ". " + item)
            count += 1
        time.sleep(3)
        print()
    
    if selection == "2":
        print()
        print("Website Blacklist")
        count = 1
        for item in blacklist:
            print(str(count) + ". " + item)
            count += 1
        time.sleep(3)
        print()
        
    if selection == "3":
        print()
        adding = False
        while not adding:
            print("Add a site to which list?")
            print("1. Whitelist")
            print("2. Blacklist")
            print()
            
            addSelection = input("Enter a selection: ")
            
            if addSelection == "1":
                site = input("Enter the site: ")
                whitelist.add(site)
                print()
                print("Whitelist")
                count = 1
                for item in whitelist:
                    print(str(count) + ". " + item)
                    count += 1
                time.sleep(3)
                print()
                adding = True
                break
                    
            if addSelection == "2":
                site = input("Enter the site: ")
                blacklist.add(site)
                print()
                print("Blacklist")
                count = 1
                for item in blacklist:
                    print(str(count) + ". " + item)
                    count += 1
                time.sleep(3)
                print()
                adding = True
                break
                
    if selection == "4":
        print()
        discarding = False
        while not discarding:
            print("Discard a site from which list?")
            print("1. Whitelist")
            print("2. Blacklist")
            print()
            
            addSelection = input("Enter a selection: ")
            
            if addSelection == "1":
                count = 1
                for item in whitelist:
                    print(str(count) + ". " + item)
                    count += 1
                site = input("Enter the URL: ")
                whitelist.discard(site)
                print()
                print("Whitelist")
                count = 1
                for item in whitelist:
                    print(str(count) + ". " + item)
                    count += 1
                time.sleep(3)
                print()
                discarding = True
                break
                    
            if addSelection == "2":
                count = 1
                for item in blacklist:
                    print(str(count) + ". " + item)
                    count += 1
                site = input("Enter the URL: ")
                blacklist.discard(site)
                print()
                print("Blacklist")
                count = 1
                for item in blacklist:
                    print(str(count) + ". " + item)
                    count += 1
                time.sleep(3)
                print()
                discarding = True
                break
        
        
    if selection == "5":
        print("Common Sites")
        dupes = blacklist.intersection(whitelist)
        count = 1
        for item in dupes:
            print(str(count) + ". " + item)
            count+= 1
        time.sleep(3)
        print()
    
    if selection == "6":
        print("Unique Sites (Single List)")
        uniques = blacklist.symmetric_difference(whitelist)
        count = 1
        for item in uniques:
            print(str(count) + ". " + item)
            count+= 1
        time.sleep(3)
        print()
 
    if selection == "7":
        print("Unique Sites (by list)")
        count = 1
        print("Blacklist Uniques")
        for item in blacklist:
            if item not in whitelist:
                print(str(count) + ". " + item)
                count += 1
        time.sleep(3)
        print()
        count = 1
        print("Whitelist Uniques")
        for item in whitelist:
            if item not in blacklist:
                print(str(count) + ". " + item)
                count += 1
        time.sleep(3)
        print()
                
    if selection == "8":
        finished = True