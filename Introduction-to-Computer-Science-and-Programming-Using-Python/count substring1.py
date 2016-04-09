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
s = 'ebobbkbsobboboboobobobbbobbobbobbhpzkcobob'
count = 0
i = -1
for c in s:
    i += 1
    if c == 'b':
        if s[i:i+3] == 'bob':
            count += 1
print "Number of times 'bob' occurs is: ",count
