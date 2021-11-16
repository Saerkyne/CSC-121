# Program: 09_inputIfElse.py
# Author: Joel Hubbard
# Date: 8/21/2021
# Purpose: Demo input and if else

flavors=input('How may flavors of ice cream do you offer: ')

numflavors = int(flavors)

if (numflavors >= 1) and (numflavors <= 32):
    if numflavors == 1:
        print('I bet it is Vanilla.')
    if numflavors == 2:
        print('I bet it is Vanilla and Chocolate.')
    if numflavors >= 3 and numflavors < 32:
        print('Ice cream selection is ok.')
    if numflavors == 32:
        print('Nice selection!!')
        
else:
    print('I did not plan for that number of flavors')