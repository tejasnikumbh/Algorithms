# Importing standard libraries
import sys
import fractions
from math import ceil
from math import sqrt

# Parsing functions 
'''
    Reads in an integer from stream passed in as the parameter. Simple
    parsing function that can read from files as well as standard input
''' 
def parseInt(stream):
    return int(stream.readline().rstrip())

'''
    Generates factors of a particular number by iterating through the num
    upto sqrt(num) . Efficient approach using prime factor generation. The
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
    Core Function. Checks if a number is both even as well as a perfect 
    square. Returns true if yes, False other wise via a boolean comparison
'''
def isEvenPerfectSquare(n):
    return n % 2 == 0 and ceil(sqrt(n)) == sqrt(n)

# Main function for the program
if __name__ == "__main__":
    stream = sys.stdin
    t = parseInt(stream)
    for i in range(t):
        n = parseInt(stream)
        f = genFactors(n)
        f.remove(n)
        reqDiv = 0
        allDiv = len(f)
        for i in f:
            if(isEvenPerfectSquare(i)):
                reqDiv += 1
        
        prob = fractions.Fraction(reqDiv,allDiv)
        prob = str(prob)
        print prob
        
