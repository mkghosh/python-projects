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
#radiationExposure(0, 5, 1)
#39.10318784326239
#radiationExposure(5, 11, 1)
#22.94241041057671
#radiationExposure(0, 11, 1)
#62.0455982538
#radiationExposure(40, 100, 1.5)
#0.434612356115



def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.

    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to
      between start and stop times.
    '''
    k = range(start,stop,step)




