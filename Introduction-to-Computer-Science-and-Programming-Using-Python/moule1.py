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
"""
The greatest common divisor of two positive integers is the largest integer that
divides each of them without remainder. For example,

    gcd(2, 12) = 2

    gcd(6, 12) = 6

    gcd(9, 12) = 3

    gcd(17, 12) = 1

Write an iterative function, gcdIter(a, b), that implements this idea.
One easy way to do this is to begin with a test value equal to the smaller of the two
input arguments, and iteratively reduce this test value by 1 until you either reach a
case where the test divides both a and b without remainder, or you reach 1.
"""
def gcd(x,y):
    if x < y:
        while x >= 1:
            if y % x == 0:
                print x
                break
            else:
                x -= 1
    else:
        while y >= 1:
            if x % y == 0:
                print y
                break
            else:
                y -= 1

gcd(13,12)
gcd(14,7)
