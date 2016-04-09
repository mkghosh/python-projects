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
def powerRecur(X,Y):
    if Y == 0:
        return 1
    else:
        return X*powerRecur(X,Y-1)
print powerRecur(2,4)
