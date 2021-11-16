# Author: Joel Hubbard
# Date: 07-Nov-2021
# Purpose:
"""
Create an Object Oriented Program that outputs the amount of each
payment for a loan. The program should ask the user for the amount of the loan, 
interest rate, and number of years.  The program should be able to set interest rate, 
the number of years and the principle.  The program should uses the monthly rate, 
number of months and the principal to calculate the payment amount. The program 
should allow the payment amount to be accessed.

Formula
payment = principal*(monthlyRate/(1- (1 + monthlyRate)**(-months)))
""" 

class Loan(object):
    def __init__(self, init_principal, init_rate, init_years):
        self.principal = int(init_principal)
        self.rate = float(init_rate)
        self.years = int(init_years)

    def __str__(self):
        return "The principal is $" + str(self.principal) + ", the rate is " + str(self.rate) + ", and the time is " + str(self.years) + " years."
    
    def set_rate(self, new_rate):
        self.rate = new_rate
    def set_principal(self, new_principal):
        self.principal = new_principal
    def set_time(self, new_years):
        self.years = new_years
    
    def payment(self):
        months = self.years * 12
        payment = self.principal * (self.rate / (1 - (1 + self.rate) ** (-months)))
        return "$" + str(round(payment, 2))

principal = input("What is the amount of the loan: ")
rate = input("What is the interest rate, as a decimal: ")
time = input("What is the timeframe of the loan, in years: ")

payment = Loan(principal, rate, time)

print(payment)
print(payment.payment())