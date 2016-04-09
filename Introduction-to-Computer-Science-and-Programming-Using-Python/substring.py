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
s = 'azcbobobegghakl'
ss = s[0]
for i in range(1, len(s)):
    if (s[i] < s[i-1]):
        ss += ' '
    ss += s[i]
print 'Longest ordered substring is:', max(ss.split(), key=len)