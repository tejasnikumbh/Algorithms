#Importing standard libraries
import sys
import fractions

# Parsing functions
def parseInt(stream):
    return int(stream.readline().rstrip())

def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]

def parseString(stream):
    return stream.readline().rstrip()

def getCharList(string):
    return list(string)

'''
    
    Core function that computes the number of 1's in the vicinity
    of each element (including itself if it is a 1), and returns
    an array of such values for element at each index.
    
    Time Complexity : O(N)
    
'''
def getVTable(intList,K):
    N = len(intList)
    vTable = [0]*N
    
    if(K == N): K -= 1
        
    count = 0
    for i in range(K+1):
        if(intList[i] == 1):
            count += 1
    vTable[0] = count
   
    
    prevSum = vTable[0]
    prevElem = 0
    nextElem = 0
    index = 1
    while(index < N):
        if((index + K) < N):
            nextElem = intList[index + K]
        else:
            nextElem = 0
        if((index - K - 1) >= 0):
            prevElem = intList[index - K - 1]
        else:
            prevElem = 0
        curSum = prevSum + nextElem - prevElem 
        prevSum = curSum
        vTable[index] = curSum
        index += 1
     
    return vTable

'''
    
    Core function. Computes the probability given how many ones
    are there in vicinity of a particular element
    
''' 
def getProb(iList,vTable):
    
    baseNum = 0
    baseDenom = len(iList) * len(iList)
    for i in range(len(iList)):
        if(iList[i] == 1):
            baseNum += vTable[i]
            
    prob = str(fractions.Fraction(baseNum,baseDenom))
    if(len(prob) == 1):
        prob = prob + "/" + "1"
    
    return prob

# Main function for the program
if __name__ == "__main__":
    # Specifying Input stream
    stream = sys.stdin
    # Parsing the number of test cases
    t = parseInt(stream)
    
    for i in range(t):
        
        # Parsing the input for each test case
        [n,k] = parseIntArr(stream)
        charList = getCharList(parseString(stream))
        intList = [int(x) for x in charList]
        
        # Generating the vicinity table
        vTable = getVTable(intList,k)
        
        # Printing the result to the console
        result = getProb(intList,vTable)
        print result
