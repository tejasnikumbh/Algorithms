import sys
import fractions
from math import ceil
from math import floor

def parseInt(s):
    return int(s.readline().rstrip())

def parseIntArr(s):
    return [int(x) for x in s.readline().rstrip().split()]

def getProb(a,b,c):
    ta = min(a,b)
    tb = max(a,b)
    a = ta
    b = tb
    denom = 2 * a * b
    num = -1
    if(c <= 0):
        return 0
    elif(c  >= a + b):
        return 1
    elif(c <= a):
        num = (c * c)
    elif(c <= b):
        num = (a * a) + 2 * (c - a) * a 
    else:
        base = a + b - c    
        num = ( (a * a) + 2 * (b - a) * a \
               + a * a - base * base )
       
    return fractions.Fraction(num,denom)    

if __name__ == "__main__":
    stream = sys.stdin
    t = parseInt(stream)
    for i in range(t):
        [a,b,c] = parseIntArr(stream)
        result = getProb(a,b,c)
        resultStr = str(result)
        if(resultStr == "1"):
            resultStr = resultStr + "/1"
        print resultStr
