#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      ThE NoViCE
#
# Created:     08/09/2014
# Copyright:   (c) ThE NoViCE 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#test 1
balance = 3329
yearlyRate = 0.2
#Test Case 2
#balance = 4773
#yearlyRate = 0.2
#Test Case 3
#balance = 3926
#annualInterestRate = 0.2
monthlyPayment = 10
while True:
    for i in range(1,13):
        remainingBalance = balance - monthlyPayment
        balance = remainingBalance + (remainingBalance*(yearlyRate/12.0))
    if balance >= 0:
        monthlyPayment += 10
    else:
        print balance
        print "Monthly paid Balance should be:" + str(monthlyPayment)
        break

