#-------------------------------------------------------------------------------
# Name:        module2
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


monthlyInterestRate = annualInterestRate/12
monthlyPayment = 0
newbalance = balance
while newbalance > 0:
    monthlyPayment += 10
    newbalance = balance
    month = 1

    while month <= 12 and newbalance > 0:
        newbalance -= monthlyPayment
        interest = monthlyInterestRate * newbalance
        newbalance += interest
        month += 1
    newbalance = round(newbalance,2)

