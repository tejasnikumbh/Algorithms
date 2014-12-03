# Importing libraries
import sys;
from math import floor;
from math import sqrt;

'''
    Function that returns a boolean indicating if number is fibo or not. The 
    mathematical trick is, if 5*n*n + 4 or 5*n*n - 4 is a perfect square, then
    the number is fibonacci
'''
def isFibo(n):
    a = 5*i*i + 4
    b = 5*i*i - 4
    if(isPerfectSquare(a) or isPerfectSquare(b)):
        return True
    
'''
    Function to determine if a number is a perfect square
'''    
def isPerfectSquare(a):
    if(floor(sqrt(a)) == sqrt(a)): 
        return True
    else: 
        return False
    
'''
    Main Function that is called by Python Interpreter
'''    
if __name__ == "__main__":
    cases = [int(x) for x in sys.stdin.readlines()];
    cases = cases[1:];
    for i in cases:
        if(isFibo(i)):
            print "IsFibo"
        else:
            print "IsNotFibo"