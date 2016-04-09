#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ThE NoViCE
#
# Created:     07/09/2014
# Copyright:   (c) ThE NoViCE 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
s = raw_input("write a sequence of character")
new_list = list(s)
number_of_vowels = 0
for character in new_list:
    if character in "aeiou":
        number_of_vowels += 1
print "Number of vowels: " + str(number_of_vowels)