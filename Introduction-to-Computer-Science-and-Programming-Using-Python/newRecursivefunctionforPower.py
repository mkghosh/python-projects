#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ThE NoViCE
#
# Created:     11/09/2014
# Copyright:   (c) ThE NoViCE 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
#The function recurPower(base, exp) from Problem 2 computed baseexp by decomposing the problem into one recursive case and one base case:

#baseexpbaseexp==base?baseexp?11ifexp>0ifexp=0
#Another way to solve this problem just using multiplication (and remainder) is to note that

#baseexpbaseexpbaseexp===(base2)exp2base?baseexp?11ifexp>0andexpisevenifexp>0andexpisoddifexp=0

#Write a procedure recurPowerNew which recursively computes exponentials using this idea.
def recurPower(base,exp):
    if exp == 0:
        return 1
    elif (base%2 == 0):
        return base*base*recurPower(base,exp/2)
    else:
        return base*recurPower(base,exp - 1)

print recurPower(3,0)
print recurPower(3,4)
print recurPower(3,3)
