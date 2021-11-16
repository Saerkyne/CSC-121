#Program: 06_typeCasting.py
#Author: Joel Hubbard
#Date: 8/21/2021
#Purpose: To display to the console the type cast value of
#         numbers stored in variables

num1 = int(1)
num2 = int(2.8)
num3 = int("3")

print(num1,num2,num3)
print("Type of the number stored in num1 is: ", type(num1))
print("Type of the number stored in num2 is: ", type(num2))
print("Type of the number stored in num3 is: ", type(num3))

num1 = float(1)
num2 = float(2.8)
num3 = float("3")
num4 = float("4.2")

print(num1,num2,num3,num4)
print("Type of the number stored in num1 is: ", type(num1))
print("Type of the number stored in num2 is: ", type(num2))
print("Type of the number stored in num3 is: ", type(num3))
print("Type of the number stored in num4 is: ", type(num4))

num1 = str(1)
num2 = str(2.8)
num3 = str("3")
num4 = str("4.2")

print(num1,num2,num3,num4)
print("Type of the number stored in num1 is: ", type(num1))
print("Type of the number stored in num2 is: ", type(num2))
print("Type of the number stored in num3 is: ", type(num3))
print("Type of the number stored in num4 is: ", type(num4))