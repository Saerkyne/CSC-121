#Program: a01_mathematicalCalculatons.py
#Author: Joel Hubbard
#Date: 8/21/2021
#Purpose: To display to the console mathematical operations
#         on two random whole numbers and two random floating
#         point numbers
import random

#Number generation and informing user of values
randWholeOne = random.randrange(1,10)
print("The first whole number is: ", randWholeOne)
randWholeTwo = random.randrange(1,10)
print("The second whole number is: ", randWholeTwo)
randFloatOne = round(random.uniform(1,10), 2)
print("The first floating point number (rounded down) is: ", randFloatOne)
randFloatTwo = round(random.uniform(1,10), 2)
print("The second floating point number (rounded down) is: ", randFloatTwo)

#Addition operations
print("\nAddition:")
wholeAddition = randWholeOne + randWholeTwo
print(str(randWholeOne) + " plus " + str(randWholeTwo) + " equals " + str(wholeAddition))
floatAddition = randFloatOne + randFloatTwo
print(str(randFloatOne) + " plus " + str(randFloatTwo) + " equals " + str(round(floatAddition, 2)))

#Subtraction operations
print("\nSubtraction:")
wholeSubtraction = randWholeOne - randWholeTwo
print(str(randWholeOne) + " minus " + str(randWholeTwo) + " equals " + str(wholeSubtraction))
floatSubtraction = randFloatOne - randFloatTwo
print(str(randFloatOne) + " minus " + str(randFloatTwo) + " equals " + str(round(floatSubtraction, 2)))

#Multiplication operations
print("\nMultiplication:")
wholeMultiplication = randWholeOne * randWholeTwo
print(str(randWholeOne) + " times " + str(randWholeTwo) + " equals " + str(wholeMultiplication))
floatMultiplication = randFloatOne * randFloatTwo
print(str(randFloatOne) + " times " + str(randFloatTwo) + " equals " + str(round(floatMultiplication, 2)))

#Division operations
print("\nDivision:")
wholeDivision = randWholeOne / randWholeTwo
print(str(randWholeOne) + " divided by " + str(randWholeTwo) + " equals " + str(wholeDivision))
floatDivision = randFloatOne / randFloatTwo
print(str(randFloatOne) + " divided " + str(randFloatTwo) + " equals " + str(round(floatDivision, 2)))

#Modulus operations
print("\nModulus:")
wholeModulus = randWholeOne % randWholeTwo
print(str(randWholeOne) + " mod by " + str(randWholeTwo) + " equals " + str(wholeModulus))
floatModulus = randFloatOne % randFloatTwo
print(str(randFloatOne) + " mod by " + str(randFloatTwo) + " equals " + str(round(floatModulus, 2)))

#Exponential operations
print("\nExponential:")
wholeExponential = randWholeOne ** randWholeTwo
print(str(randWholeOne) + " raised to " + str(randWholeTwo) + " equals " + str(wholeExponential))
floatExponential = randFloatOne ** randFloatTwo
print(str(randFloatOne) + " raised to " + str(randFloatTwo) + " equals " + str(round(floatExponential, 2)))