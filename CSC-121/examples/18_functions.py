

#  Program: 18_functions.py
#  Author: Michael Souther
#  Date: 09/28/2020
#  Create a function to out a verse of Old MacDonald had a farm
def oldMacVerse(animal, sound):
    """Outputs a verse of Old MacDonald using arguments."""
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, oh!")
    print("And on his farm he had a ", animal, " Ee-igh, Ee-igh, oh!")
    print("With a ", sound, " ", sound, " here ")
    print("And a ", sound, " ", sound, " There ")
    print("And a Moo Moo there")
    print("Here a ", sound, " , there a ", sound, " ,  everywhere a ", sound, " ", sound,)
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, oh!")

oldMacVerse("Cow", "Moo")
print()
oldMacVerse("Pig", "Oink")
print()
oldMacVerse("Chicken", "Cluck")
print()
oldMacVerse("Duck", "Quack")