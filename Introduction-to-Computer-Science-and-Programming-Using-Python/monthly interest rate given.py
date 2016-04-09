#-------------------------------------------------------------------------------
# Name:        module1
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
balance = int(raw_input('Put a integar value your debt'))
annualInterestRate = float(raw_input("put the annual interest rate of your bank"))
monthlyPaymentRate = float(raw_input("Your monthly min Payment rate"))
paymentOfEachMonth = []
remainingBalance = 0
for i in range(1,13):
    minPayment = 0
    minPayment = balance*monthlyPaymentRate
    remainingBalance = balance-minPayment
    paymentOfEachMonth.append(minPayment)
    balance = remainingBalance + (remainingBalance*(annualInterestRate/12.0))
    print "Month: " + str(i)
    print "Minimum monthly payment: " +"{:.2f}".format(minPayment)
    print "Remaining balance: " + "{:.2f}".format(balance)
print "Total paid: " + str(sum(paymentOfEachMonth))
print "Remaining balanc: " + str(balance)
