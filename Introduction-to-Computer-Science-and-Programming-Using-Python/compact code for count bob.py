#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ThE NoViCE
#
# Created:     10/09/2014
# Copyright:   (c) ThE NoViCE 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
s = "bobob"
countBob = 0
while "bob" in s:
    s = s.replace("bob",'b',1)
    countBob += 1
print "Number of times bob occurs" + str(countBob)
