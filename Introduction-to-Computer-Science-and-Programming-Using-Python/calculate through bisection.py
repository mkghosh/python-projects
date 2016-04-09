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
balance = 320000
annualInterestRate = 0.2
bal = balance
LB = (balance)/12.0
UB = (balance*(1 + (annualInterestRate/12.0)**12))
while abs(bal) > 0.1:
    bal = balance
    LP = round((UB + LB) / 2.0,2)
    for mnth in range(12):
        bal = (bal -LP )*(1+annualInterestRate/12)
    if bal > 0:
        LB = LP
    else:
        UB = LP
print "Lowest payment:",LP