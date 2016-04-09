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

s = 'azcbobobegghakl'
r=''
c=''
for char in s:
 if(c==''):
  c=char
 elif(c[-1]<=char):
  c+=char
 elif(c[-1]>char):
  if(len(r)<len(c)):
   r=c
   c=char
  else:
   c=char
if(len(c)>len(r)):
 r=c
print(r)