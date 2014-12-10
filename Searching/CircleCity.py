# Importing standarad libraries
import sys

'''
    Generates factors of a particular number by iterating through the num
    upto num / 2 . Efficient approach using prime factor generation. The
    function reduce if new to you, just computes result of the supplied
    function f (in this case list.__add__) on the first two elements of the
    supplied list, obtains a result and then performs the same function on
    the result and the next element in the list. In this way it reduces the 
    entire list to one result
'''
def genFactors(n):    
    return set(reduce(list.__add__, 
                [ [i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0 ] ) )

'''
    This function returns the number of integral solutions for the 
    equation x^2 + y^2 = r , given x, y and r. The number of integral
    solutions to this equation is related to the factors of r.
    Firstly , let f = Set of factors of r
    Discard all even factors of r. Let new set craeted be fOdd
    Let C1 = factors in fOdd that yield 1 when modulo by 4
    Let C3 = factors in fOdd that yield 3 when modulo by 4
    Then the number of integral solutions is C1 - C3. 
    Let I = C1 - C3
    
    Notes : 
    1. If x,y and y,x are distinct then Integral Solution pairs = I
    else they are I/2
    2. If we are talking about a circle, the above disucssion is pert
    -inent only to one quadrant(since it is simply numerical computation)
    therefore, we need to multiply it by 4 to get all solutions.In that
    case Total Integral Solutions = 4 * I
    
'''
def getGaussBorderNum(r):
    f = genFactors(r)
    fOdd = [x for x in f if x % 2 != 0 ]
    C1 = [x for x in fOdd if x % 4 == 1]
    C3 = [x for x in fOdd if x % 4 == 3]
    return 4* (len(C1) - len(C3))

'''
    Main function to run the program. Logic is pretty simple in the 
    fact that we need to find the integral number of solutions to the
    circle equation and check if the number is less than k or not
'''
if __name__ == "__main__":
    t = int(sys.stdin.readline().rstrip())
    for i in range(t):
        [r,k] = [int(x) for x in sys.stdin.readline().rstrip().split()]
        num = getGaussBorderNum(r)
        if(k<num):
            print "impossible"
        else:
            print "possible"