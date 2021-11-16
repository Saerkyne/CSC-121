#Program: 05_math.py
#Author: Joel Hubbard
#Date: 8/21/2021
#Purpose: To demo math operations

value1=int(input("Enter the first value: "))
value2=int(input("Enter the second value: "))

addValue=value1+value2
print(str(value1) + " plus " + str(value2) + " equals " + str(addValue))

subtractValue=value1 - value2
print(str(value1) + " minus " + str(value2) + " equals " + str(subtractValue))

multiplyValue=value1 * value2
print(str(value1) + " times " + str(value2) + " equals " + str(multiplyValue))

divideValue=value1 / value2
print(str(value1) + " divided by " + str(value2) + " equals " + str(divideValue))

modValue = value1 % value2
print(str(value1) + " mod by " + str(value2) + " equals " + str(modValue))