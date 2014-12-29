# Importing standard libraries
import sys

# Parsing functions
def parseInt(stream):
    return int(stream.readline().rstrip())

def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]

'''
    
    Function that returns the total number of minimum operations required.
    This has three conceptual aspects. 
    1. Adding choclates to everyone else except one by a number N is equal 
    to subtracting choclates from that one person by N. This is because we
    only are concerned with OPERATIONS for equalizing number of choclates 
    of everybody.
    2. There is an optimum minimum level.(minimum number of chochlates).
    This can be either the min of the entire numbers of choclates with peo
    -ple initially, or anything in range [fMin, fMin - 5]. It can't go bey
    -onod that because it will always require an extra operation since the
    max greedy reaching way(subtraction amount of choclates) is 5.
    3. for any level between fMin to fMin - 5, we make each person reach
    there by subtracting choclates in a greedy way. Say if the chocs ini
    -tially are k, we reach by k/5 + (k%5)/2 + (k%5)%2 . We compute such
    steps for all people are compute total number of operations in this way.
    FINALLY, we do this for the range fMin to fMin - 5 and compute the
    min of this and return this as the answer.
    
'''
def getMinOper(NArr):
    NArr.sort()
    minVal = NArr[0]
    results = []
    for val in range(minVal - 5, minVal + 1):
        results.append(getMin(NArr,val))
    return min(results)

def getMin(A,minVal):
    count = 0
    for k in A:
        count += getOperGreedy(k,minVal)
    return count

def getOperGreedy(k,minVal):
    k = k - minVal
    opers = 0
    opers += k/5
    opers += (k%5)/2
    opers += (k%5)%2
    return opers

# Main function for the program
if __name__ == "__main__":
    stream = sys.stdin
    T = parseInt(stream)
    for i in range(T):
        N = parseInt(stream)
        NArr = parseIntArr(stream)
        NMinOper = getMinOper(NArr)
        result = NMinOper
        print result
