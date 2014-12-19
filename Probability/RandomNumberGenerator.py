# Importing standard libraries
import sys
import fractions

'''
    Parsing function that parses an int from given stream
'''
def parseInt(s):
    return int(s.readline().rstrip())

'''
    Parsing function that parses an integer array from given stream
'''
def parseIntArr(s):
    return [int(x) for x in s.readline().rstrip().split()]

'''
    First we find the probability distribution of a sum of two uniform
    random variables. This is done by convoluting their respective pdfs
    Once this is done, value of P(x+y < C) is computed using the cdf of 
    the function and output is returned in Fractional form.
'''
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

'''
    Main function to run the program
'''
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
