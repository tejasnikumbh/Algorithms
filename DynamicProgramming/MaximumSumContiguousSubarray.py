# Importing standard libraries
import sys

'''
    Reads in an integer from stream passed in as the parameter. Simple
    parsing function that can read from files as well as standard input
'''
def parseInt(stream):
    return int(stream.readline().rstrip())
'''
    Reads in an array of integers from stream passed in as parameter.This
    is a simple parsing function that can read from files as well as
    standard input
'''
def parseIntArr(stream):
    return [int(x) for x in stream.readline().rstrip().split()]


'''
    Function to print the array with numbers in a space seperated format
'''
def printArray(a,delimiter):
    arrayStr = ""
    for i in a:
        arrayStr += str(i) + delimiter
    arrayStr.rstrip()
    print arrayStr

'''
    Applying K-dane's algorithm to get the maximum contiguous subarray
    Sum in the array passed in as parameter. If all elements non positive
    then return the max of the numbers in the array
'''
def getMaxContiguous(a):
    if(allNonPos(a)):
        return max(a)
    else:
        maxEndingHere = maxSoFar = 0
        for i in a:
            maxEndingHere += i
            if(maxEndingHere < 0): maxEndingHere = 0
            maxSoFar = max(maxEndingHere,maxSoFar)
        return maxSoFar
        
'''
    Simply the sum of all positive numbers in array. If all are non 
    Positive return the max of the numbers in the array
'''    
def getMaxNonContiguous(a):
    if(allNonPos(a)):
        return max(a)
    else:
        return sum([x for x in a if x>0])
'''
    Returns True if all elements in array are 0 or negative.(non postive)
'''    
def allNonPos(a):
    for i in a:
        if(i > 0):
            return False;
    return True

'''
    Main function for the program
'''
if __name__ == "__main__":
    stream = sys.stdin
    t = parseInt(stream)
    for i in range(t):
        lenA = parseInt(stream)
        a = parseIntArr(stream)
        ans = [-1,-1]
        ans[0] = getMaxContiguous(a)
        ans[1] = getMaxNonContiguous(a)
        printArray(ans," ")
        
