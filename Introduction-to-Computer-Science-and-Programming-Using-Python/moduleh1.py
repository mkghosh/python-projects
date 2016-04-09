#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ThE NoViCE
#
# Created:     09/09/2014
# Copyright:   (c) ThE NoViCE 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#test 1
balance = 3329
annualInterestRate = 0.2
#Test Case 2
balance = 4773
#annulInterestRate = 0.2
#Test Case 3
#balance = 3926
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
#annualInterestRate = 0.2
#balance = 3329
monthlyPayment = 10
monthlyInterestRate = annualInterestRate /12
newbalance = balance - 10

while abs(remainBalance)> 0.1:
    remainBalance = balance
    lowestPayment = round((lowerBound+upperBound)/2.0,2)
    for month in range(12):
        remainBalance = (remainBalance - lowestPayment)*(1+annualInterestRate/12)
    if remainBalance > 0:
        lowerBound = lowestPayment
    else:
        upperBound = lowestPayment
print "the value of lowest payment", lowestPayment