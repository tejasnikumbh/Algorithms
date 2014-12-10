# Importing standard libraries
import sys

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
    Space Efficient Counting sort version. Sorts using regular counting sort 
    algorithm except for the fact there is wrapping and unwrapping of vlaues
    in the array to make space efficient frequency Table in the counting sort
    Time Complexity = O(N)
    Space Complexity = O(Max - Min)
'''    
def unWrapIndex(i,minVal):
    return i + minVal

def wrapIndex(i,minVal):
    return i - minVal

def boundCountingSort(a):
    XMin = min(a)    
    XMax = max(a)
    b = [0] * (XMax - XMin + 1)
    for i in a:
        index = wrapIndex(i,XMin)
        b[index] += 1
    sortedArr = []
    for i in range(len(b)):
        for j in range(b[i]):
            element = unWrapIndex(i,XMin)
            sortedArr.append(element)
    return b,sortedArr

'''
    Main function to run the program. We simply calculate the
    frequency diff based on logic used in counting sort which 
    enables us to run this algo in O(N) time
'''
if __name__ == "__main__":
    aSize = sys.stdin.readline().rstrip()
    a = [int(x) for x in sys.stdin.readline().rstrip().split()]
    bSize = sys.stdin.readline().rstrip()
    b = [int(x) for x in sys.stdin.readline().rstrip().split()]
    [freqArray,sortedArray] = boundCountingSort(b)
    # Computing the missing elements. Logic used is decrease 
    # frequency of elements existing in a in the frequency table of
    # the array b . Frequency table was returned above
    bMin = min(b)
    bMax = max(b)
    outputArr = []
    for i in a:
        index = wrapIndex(i,bMin)
        freqArray[index] -= 1
    for i in range(len(freqArray)):
        element = unWrapIndex(i,bMin)
        for j in range(freqArray[i]):
            outputArr.append(element)
    # Need to print missing numbers only once, hence set used
    outputArr = list(set(outputArr))
    # Need to print in ascending order, hence sorting used
    outputArr.sort()
    # Printing the result to the console
    printArray(outputArr," ")       